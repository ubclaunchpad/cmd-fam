from flask import Flask

from service.VideoDownload import VideoDownload

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/video/youtube', methods=["POST"])
def youtube_video(request):
    VideoDownload(request.get_json()).fetch_transcript_youtube()
    return 'Fetched youtube video script'


if __name__ == '__main__':
    app.run(debug=True, port=8050)
