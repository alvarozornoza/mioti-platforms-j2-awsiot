import time
import json
import random
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import winsound
# LINUX import os

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, TOPIC, and RANGE
ENDPOINT = "X.iot.eu-west-3.amazonaws.com"
CLIENT_ID = "simulator01"
PATH_TO_ROOT = "../certificates/AmazonRootCA1.pem"
PATH_TO_CERT = "../certificates/certificate.pem.crt"
PATH_TO_KEY = "../certificates/private.pem.key"
TOPIC = "devices/simulator01/telemetry"
RANGE = 20

def beep():
    duration = 50  # milliseconds
    # LINUX duration = 1  # seconds
    freq = 1000  # Hz
    winsound.Beep(freq, duration)

def customCallback(client, userdata, message):
    payload = json.loads(message.payload)
    temperature = payload["temperature"]

    if(temperature > 28):
        beep()
        # os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

def main():
    client = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
    client.configureEndpoint(ENDPOINT, 8883)
    client.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)
    client.connect()
    client.subscribe(TOPIC, 1, customCallback)

    loopCount = 0
    while True:
        loopCount += 1
        
    client.disconnect()

if __name__ == '__main__':
    main()

