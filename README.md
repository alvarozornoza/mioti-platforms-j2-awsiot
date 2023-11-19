# mioti-platforms-j2-awsiot
## Clonar repositorio
```
git clone https://github.com/alvarozornoza/mioti-platforms-j2-awsiot.git
```
## Crear dispositivo AWS IOT core
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Receive"
      ],
      "Resource": [
        "arn:aws:iot:eu-west-3:552240702490:topic/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": [
        "arn:aws:iot:eu-west-3:552240702490:topicfilter/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": [
        "arn:aws:iot:eu-west-3:552240702490:client/*"
      ]
    }
  ]
}
```

## Crear virtual environment e instalar requirements

### Windows 10

```
cd mioti-platforms-j2-awsiot/simulator
py -m pip install virtualenv
py -m venv .venv
.\venv\Scripts\activate
py -m pip install -r requirements.txt

deactivate
```

### Linux 
```
cd mioti-platforms-j2-awsiot/simulator
sudo apt-get install python-pip

pip install virtualenv
// sudo apt install virtualenv

virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip3 install -r requirements.txt

deactivate
```

## Crear S3 bucket
### Policy
```
 {
     "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRea2411145d",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::alvarobucketiot/*"
        }
    ]
}
```

## CORS
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 6000
    }
]
```

## Establecer IOT rule
```
SELECT *,timestamp() AS timestamp FROM 'devices/+/telemetry'
```

Key: ${topic(2)}