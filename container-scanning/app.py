from flask import Flask, request
from waitress import serve
# from azure.storage.queue import QueueClient, TextBase64EncodePolicy
import pika
import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# import config.config_variables

app = Flask(__name__)
 

@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
        response = request.get_json()
        credentials = pika.PlainCredentials("admin", "admin")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.171.129.95", credentials=credentials))
        channel = connection.channel()
        massage = response["target"]["repository"]
        channel.queue_declare(queue="logs")
        channel.basic_publish(exchange='',
                              routing_key="logs",
                              body=massage)
        connection.close() 
        return "success!"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)