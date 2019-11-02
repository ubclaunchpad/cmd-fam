from __future__ import unicode_literals
from youtube_transcript_api import YouTubeTranscriptApi
import json


class VideoDownload:
    def __init__(self, request):
        self.id = request['videoId']
        self.script = {}

    def fetch_transcript_youtube(self):
        try:
            self.script = YouTubeTranscriptApi.get_transcript(self.id)
        except YouTubeTranscriptApi.CouldNotRetrieveTranscript:
            return json.dumps({"error": "No caption for this youtube video"}), 404
            # self.from_youtube()
        return "caption fetched"




