from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query, send_message_to_rabbitmq


app = Flask(__name__)
 

@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
        response = request.get_json()
        res = {"digest":response["target"]["digest"], "repository":response["target"]["repository"]}
        send_message_to_rabbitmq(str(res))
        result = run_resource_graph_query(response["target"]["digest"],response["target"]["repository"])
        return result


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)