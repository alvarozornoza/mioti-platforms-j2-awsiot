import time
import json
import random
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, TOPIC, and RANGE
ENDPOINT = 
CLIENT_ID = 
PATH_TO_ROOT = 
PATH_TO_CERT = 
PATH_TO_KEY = 
TOPIC = 
RANGE = 

def main():
    client = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    client.configureEndpoint(ENDPOINT, 8883)
    client.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    client.connect()

    print('Begin Publish')
    for i in range (RANGE):
        print("Published")
    print('Publish End')
    client.disconnect()

if __name__ == '__main__':
    main()