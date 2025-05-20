#  Convert MP3 to WAV and then transcribe
from pydub import AudioSegment
import speech_recognition as sr

# Step 1: Convert mp3 to wav
mp3_file = "C:/Users/pankt/Downloads/minion.mp3"
wav_file = "converted.wav"

print(" Converting MP3 to WAV...")
sound = AudioSegment.from_mp3(mp3_file)
sound.export(wav_file, format="wav")
print(" Conversion complete.")

# Step 2: Transcribe the WAV file
recognizer = sr.Recognizer()

with sr.AudioFile(wav_file) as source:
    print("🎧 Loading audio...")
    audio_data = recognizer.record(source)

try:
    print(" Transcribing...")
    text = recognizer.recognize_google(audio_data)
    print(" Transcription:\n", text)

    with open("my_transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(" Saved to my_transcription.txt")

except sr.UnknownValueError:
    print(" Could not understand audio.")
except sr.RequestError as e:
    print(f" Request failed: {e}")
