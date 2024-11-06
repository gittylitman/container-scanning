import azure.functions as func
import logging
import subprocess


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="")
def trivy(req: func.HttpRequest) -> func.HttpResponse:
    payload = req.get_json()
    logging.info(payload)
    server_acr = payload['request']['host']
    image_name = payload['target']['repository']
    image_tag = payload['target']['tag']
    full_image_name = f"{server_acr}/{image_name}:{image_tag}"
    logging.info(full_image_name)
    trivy_scan = subprocess.Popen(["trivy", "--exit-code", "0", "--format", "json", full_image_name], stdout=subprocess.PIPE)
    scan_output, _ = trivy_scan.communicate()
    logging.info(scan_output)
    return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
