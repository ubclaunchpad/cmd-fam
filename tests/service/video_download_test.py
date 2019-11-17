from service.VideoDownload import VideoDownload
from unittest import mock, TestCase
import json

class TestVideoDownload(TestCase):

    def setup(self):
        pass
    
    # TODO: Not working yet, still calling actual youtube API
    def test_fetch_youtube_transcript_good_request(self):
        request_string = '{"type": "youtube","videoId": "JyA1lBJl_qM"}'
        request = json.loads(request_string)
        videoDownloader = VideoDownload(request)
        YoutubeTranscriptAPI = mock.MagicMock()
        YoutubeTranscriptAPI.get_transcript.return_value = "stuff"
        transcript = videoDownloader.fetch_transcript_youtube()
        assert "stuff" == transcript
    
    def test_fetch_youtube_transcript_bad_request(self):
        request_string = '{"type": "youtube","videoId": "JyA1lBJl_qM"}'
        request = json.loads(request_string)
        videoDownloader = VideoDownload(request)
        YoutubeTranscriptAPI = mock.MagicMock(side_effect=KeyError('foo'))
        YoutubeTranscriptAPI.get_transcript.return_value = "stuff"
        transcript = videoDownloader.fetch_transcript_youtube()
        assert (json.dumps({"error": "No caption for this youtube video"}), 404), transcript