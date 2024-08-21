from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query


app = Flask(__name__)
 

@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
        response = request.get_json()
        run_resource_graph_query("sha256:404a0f601f670d7670b4b2590da726fd52b482954b3163d6c13da11e98fa4964","newspace")
        # run_resource_graph_query(response["target"]["digest"],response["target"]["repository"])
        return "success!"


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)