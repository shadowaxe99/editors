```python
import unittest
import os
from editor.utils import allowed_file, save_video_file, generate_thumbnail, transcribe_audio, analyze_sentiment, optimize_content

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.test_video_path = 'data/videos/test_video.mp4'
        self.test_thumbnail_path = 'data/thumbnails/test_thumbnail.png'
        self.test_transcript_path = 'data/transcripts/test_transcript.txt'
        self.test_video_metadata = {
            "title": "Test Video",
            "description": "A test video description",
            "tags": ["test", "video"],
            "category": "Education",
            "visibility": "public"
        }

    def test_allowed_file(self):
        self.assertTrue(allowed_file('test_video.mp4'))
        self.assertFalse(allowed_file('test_video.txt'))

    def test_save_video_file(self):
        # Assuming save_video_file function returns the path where the file is saved
        with open(self.test_video_path, 'wb') as f:
            f.write(os.urandom(124))  # Write random bytes to create a dummy file
        self.assertEqual(save_video_file(self.test_video_path), self.test_video_path)
        os.remove(self.test_video_path)  # Clean up after test

    def test_generate_thumbnail(self):
        # Assuming generate_thumbnail function returns the path of the generated thumbnail
        self.assertEqual(generate_thumbnail(self.test_video_path), self.test_thumbnail_path)

    def test_transcribe_audio(self):
        # Assuming transcribe_audio function returns the path of the transcript file
        self.assertEqual(transcribe_audio(self.test_video_path), self.test_transcript_path)

    def test_analyze_sentiment(self):
        # Assuming analyze_sentiment function returns a sentiment score
        sentiment_score = analyze_sentiment(self.test_video_path)
        self.assertIsInstance(sentiment_score, float)
        self.assertGreaterEqual(sentiment_score, 0.0)
        self.assertLessEqual(sentiment_score, 1.0)

    def test_optimize_content(self):
        # Assuming optimize_content function returns optimized metadata
        optimized_metadata = optimize_content(self.test_video_metadata)
        self.assertIsInstance(optimized_metadata, dict)
        self.assertIn("title", optimized_metadata)
        self.assertIn("description", optimized_metadata)
        self.assertIn("tags", optimized_metadata)
        self.assertIn("category", optimized_metadata)
        self.assertIn("visibility", optimized_metadata)

if __name__ == '__main__':
    unittest.main()
```