from flask import Flask
from config import config
from requests import request
import librosaAnalysis

app = Flask(__name__)


@app.route('/api/audio', methods=['GET', 'POST'])
def get_file():
    if request.method == 'POST':
        file = request.files['messageFile']
        librosaAnalysis.analyze_file(file[0])


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
