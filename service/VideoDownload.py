"""Video Data Extractor."""
from __future__ import unicode_literals
from youtube_transcript_api import YouTubeTranscriptApi
import json


class VideoDownload:
    """Data extractor."""

    def __init__(self, request):
        """Initialize id and transcript."""
        self.id = request['videoId']
        self.script = {}

    def fetch_transcript_youtube(self):
        """Fetch transcript."""
        try:
            self.script = YouTubeTranscriptApi.get_transcript(self.id)
        except YouTubeTranscriptApi.CouldNotRetrieveTranscript:
            return json.dumps({
                "error": "No caption for this youtube video"
            }), 404
        return "caption fetched"
