import requests
import config


def send_audio(filelist, url):
    # print('attempting to send audio')

    req = requests.post(url, files=filelist)
    print(req.status_code)
    print(req.text)


file1 = config.file1Location
file2 = config.file2Location

files = {'audio1': open(file1, 'rb'), 'audio2': open(file2 , 'rb')}
send_audio(files, config.localurl)

