"""Server."""

import json
from flask import Flask
from flask import request
from service.VideoDownload import VideoDownload
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    """Return main page."""
    return "Main Page"


@app.route('/video', methods=["POST"])
def video_process():
    """Process video information."""
    body = request.json
    if body['type'] == 'youtube':
        return VideoDownload(request.json).fetch_transcript_youtube()
    else:
        return json.dumps({"error": "Video type not compatible"}), 404
