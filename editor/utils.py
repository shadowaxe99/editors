```python
import os
from werkzeug.utils import secure_filename
import moviepy.editor as mp
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import io
from textblob import TextBlob

# Assuming the shared dependencies are in a separate file named shared_dependencies.py
# from shared_dependencies import UPLOAD_FOLDER, THUMBNAIL_FOLDER, TRANSCRIPT_FOLDER, EXPORT_FOLDER, ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_video_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        video_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(video_path)
        return video_path
    return None

def generate_thumbnail(video_path):
    video_clip = mp.VideoFileClip(video_path)
    thumbnail_path = os.path.join(THUMBNAIL_FOLDER, os.path.splitext(os.path.basename(video_path))[0] + '.png')
    video_clip.save_frame(thumbnail_path, t=(video_clip.duration / 2.0))  # Save frame at the middle of the video
    return thumbnail_path

def transcribe_audio(video_path, language_code='en-US'):
    client = speech.SpeechClient()
    with io.open(video_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    transcript_path = os.path.join(TRANSCRIPT_FOLDER, os.path.splitext(os.path.basename(video_path))[0] + '.txt')
    with open(transcript_path, 'w') as transcript_file:
        transcript_file.write(transcript)

    return transcript_path

def analyze_sentiment(video_path):
    transcript_path = transcribe_audio(video_path)
    with open(transcript_path, 'r') as transcript_file:
        transcript = transcript_file.read()

    analysis = TextBlob(transcript)
    sentiment = analysis.sentiment
    return sentiment.polarity, sentiment.subjectivity

def optimize_content(video_metadata):
    # Placeholder for content optimization logic
    # This could include analysis of video length, posting time, etc.
    # For now, we'll just return the metadata unchanged
    return video_metadata
```