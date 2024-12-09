# config.py

import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FOLDER = os.path.join(BASE_DIR, "audio_files/")
TRANSCRIPTION_FOLDER = os.path.join(BASE_DIR, "transcriptions/")

# Ensure folders exist
os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPTION_FOLDER, exist_ok=True)

# Supported Audio Formats
SUPPORTED_FORMATS = (".wav", ".flac", ".m4a")