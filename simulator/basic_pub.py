import time
import json
import random
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, TOPIC, and RANGE
ENDPOINT = "X.iot.eu-west-3.amazonaws.com"
CLIENT_ID = "simulator01"
PATH_TO_ROOT = "../certificates/AmazonRootCA1.pem"
PATH_TO_CERT = "../certificates/certificate.pem.crt"
PATH_TO_KEY = "../certificates/private.pem.key"
TOPIC = "devices/simulator01/telemetry"
RANGE = 200 

def main():
    client = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    client.configureEndpoint(ENDPOINT, 8883)
    client.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    client.connect()

    print('Begin Publish')
    for i in range (RANGE):
        temperature = round(random.uniform(20, 30), 2)
        humidity = round(random.uniform(40, 50), 2)
        message = {"temperature" : temperature, "humidity": humidity}
        client.publish(TOPIC, json.dumps(message), 1)
        print("Published: '" + json.dumps(message) + "' to the topic: " + TOPIC)
        time.sleep(2)

    print('Publish End')
    client.disconnect()

if __name__ == '__main__':
    main()