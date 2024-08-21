from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query


app = Flask(__name__)
 

@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
        response = request.get_json()

        run_resource_graph_query("sha256:5cc29eaa06d5b4a478475e433341c2964eeb10559635b0dc43265fba703c05f8","aaaaaa")
        # run_resource_graph_query(response["target"]["digest"],response["target"]["repository"])
        return "success!"


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)