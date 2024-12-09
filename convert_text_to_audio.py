# text_to_speech/convert_text_to_audio.py

from gtts import gTTS

def convert_text_to_audio(text, output_path):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)
        print(f"Audio file created at: {output_path}")
    except Exception as e:
        print(f"Failed to convert text to audio: {e}")

