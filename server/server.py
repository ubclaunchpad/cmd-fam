"""Server"""

import json
from flask import Flask
from flask import request
from service.VideoDownload import VideoDownload
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route('/')
def main():
    return "Main Page"
    


@app.route('/video', methods=["POST"])
def video_process():
    body = request.json
    if body['type'] == 'youtube':
        return VideoDownload(request.json).fetch_transcript_youtube()
    else:
        return json.dumps({"error": "Video type not compatible"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=8050)
