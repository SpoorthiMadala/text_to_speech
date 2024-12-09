from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
import os

# Initialize Flask app
app = Flask(__name__)

# Folder to save generated audio files
AUDIO_FOLDER = "static/audio/"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None

    if request.method == "POST":
        try:
            text = request.form.get("text")
            if text:
                audio_path = os.path.join(AUDIO_FOLDER, "output_audio.wav")
                tts = gTTS(text)
                tts.save(audio_path)

                audio_file = f"/static/audio/output_audio.wav"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)

