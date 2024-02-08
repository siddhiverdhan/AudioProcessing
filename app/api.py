from flask import Flask
from config import config
from requests import request

app = Flask(__name__)


@app.route('/api/audio', methods=['GET', 'POST'])
def get_score():
    if request.method == 'POST':
        file = request.files['messageFile']


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
