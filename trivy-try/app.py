import subprocess

def tryv() :
    server_acr = "containerregistryautomationdev.azurecr.io"
    image_name = "trivy"
    image_tag = "latest"
    full_image_name = f"{server_acr}/{image_name}:{image_tag}"
    # trivy_scan = subprocess.Popen(["trivy", "--exit-code", "0", "--format", "json", "image", "python"], stdout=subprocess.PIPE)
    result = subprocess.Popen(['trivy', 'image', '--format', 'json', "python"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = result.communicate()  
    print("stdout")
    print(stdout)
    print("stderr")
    print(stderr)


tryv()