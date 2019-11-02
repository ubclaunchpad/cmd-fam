from flask import Flask
from flask import request
import json

from service.VideoDownload import VideoDownload

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/video/youtube', methods=["POST"])
def youtube_video():
    return VideoDownload(request.json).fetch_transcript_youtube()


if __name__ == '__main__':
    app.run(debug=True, port=8050)
