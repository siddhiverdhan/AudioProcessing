from flask import Flask, request
import librosaaudiocompare
import configuration
import json

app = Flask(__name__)


@app.route('/api/audio', methods=["POST"])
def process_files():
    if request.method == 'POST':
        file1 = request.files['audio1']
        file2 = request.files['audio2']
        data = librosaaudiocompare.compare_audio(file1, file2)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route('/api/hello', methods=["GET"])
def hello():
    print("Get api called")
    return "Hello World"


if __name__ == '__main__':
    from waitress import serve
    #app.run(host=config.host, port=config.port)
    serve(app, host=configuration.host)
