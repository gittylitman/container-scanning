from azure.identity import DefaultAzureCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest
import pika,time


def run_resource_graph_query(image_digest,image_name):
        # time.sleep(300)
        
        credential = DefaultAzureCredential()
        client = ResourceGraphClient(credential)
        query = set_resource_graph_query(image_digest, image_name)
        result = client.resources(QueryRequest(query=query)).as_dict()
        # if result["data"] == []:
        #        result["data"] = [{"image-name":image_name}, {"data":"Health check"}]
        result=str(result) 
        rabbit_massage=send_message_to_rabbitmq(result)
        return rabbit_massage




def set_resource_graph_query(image_digest,image_name):
    query = f"""
        securityresources
        | where type =~ 'microsoft.security/assessments/subassessments'
        | where properties.resourceDetails.ResourceProvider == 'acr'
        | where properties contains '{image_digest}'
        | summarize data = make_list(pack(
            'CVE_ID', properties.id,
            'Severity', properties.additionalData.vulnerabilityDetails.severity
        )) by tostring(properties.resourceDetails.ResourceName)
        | project ImageName='{image_name}' , Data=data
    """
    return query


def send_message_to_rabbitmq(message):
        credentials = pika.PlainCredentials("admin", "admin")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.171.129.95", credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue="logs")
        channel.basic_publish(exchange='',
                              routing_key="logs",
                              body=message)
        connection.close() 
        return "success!"
    


    