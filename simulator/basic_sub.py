import winsound
# LINUX import os
def beep():
    duration = 50  # milliseconds
    # LINUX duration = 1  # seconds
    freq = 1000  # Hz
    winsound.Beep(freq, duration)

def customCallback(client, userdata, message):
    payload = json.loads(message.payload)
    temperature = payload["temperature"]

def main():

if __name__ == '__main__':
    main()

