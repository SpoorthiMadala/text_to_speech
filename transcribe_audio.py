# text_to_speech/transcribe_audio.py

import speech_recognition as sr
import os

def transcribe_audio(file_path, output_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

            with open(output_path, "w") as transcription_file:
                transcription_file.write(text)
            
            print(f"Transcription saved to: {output_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

