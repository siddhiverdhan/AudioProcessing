import requests
from config import config


def send_audio(file, url):
    # print('attempting to send audio')
    with open(file, 'rb') as file:
        data = {'uuid': '-jx-1', 'alarmType': 1, 'timeDuration': 10}
        files = {'messageFile': file}

        req = requests.post(url, files=files, json=data)
        print(req.status_code)
        print(req.text)
