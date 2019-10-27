from __future__ import unicode_literals
from youtube_transcript_api import YouTubeTranscriptApi


class VideoDownload:
    def __init__(self, request):
        self.id = request['videoId']
        self.script = {}

    def fetch_transcript_youtube(self):
        try:
            self.script = YouTubeTranscriptApi.get_transcript(self.id)
        except YouTubeTranscriptApi.CouldNotRetrieveTranscript:
            pass
            # self.from_youtube()
        print(self.script)




