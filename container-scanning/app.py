from flask import Flask
from waitress import serve
from azure.storage.queue import QueueClient, TextBase64EncodePolicy
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config.config_variables

app = Flask(__name__)
 

@app.route("/image_push", methods=["POST"])
def send_to_image_scanning():
    queue_client = QueueClient.from_connection_string(
        config.config_variables.connection_string,
        config.config_variables.queue_name,
        message_encode_policy=TextBase64EncodePolicy(),
    )
    queue_client.send_message("hello world")
    return "success!"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)