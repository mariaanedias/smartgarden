import boto3
import json

client = boto3.client('iot-data', region_name='us-east-1')

def function_handler(event, context):
    # Change topic, qos and payload
    response = client.publish(
        topic='SmartGarden/WaterRelease',
        qos=0,
        payload=json.dumps({"water":"plant"})
    )
    return "I'm going to water your Smart Garden!"
