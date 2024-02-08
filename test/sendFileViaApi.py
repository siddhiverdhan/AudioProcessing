import requests
from config import config


def send_audio():
    # print('attempting to send audio')
    url = config.localurl
    with open(config.testfilelocation, 'rb') as file:
        data = {'uuid': '-jx-1', 'alarmType': 1, 'timeDuration': 10}
        files = {'messageFile': file}

        req = requests.post(url, files=files, json=data)
        print(req.status_code)
        print(req.text)
