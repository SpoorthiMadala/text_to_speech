# text_to_speech/convert_audio_to_wav.py

from pydub import AudioSegment

def convert_audio_to_wav(input_path, output_path):
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        print(f"Converted {input_path} to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"Audio conversion error: {e}")

