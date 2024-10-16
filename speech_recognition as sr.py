import speech_recognition as sr
import wave

# Initialize recognizer
r = sr.Recognizer()

# Start recording audio from the microphone
with sr.Microphone() as source:
    print("Say something...")
    audio_data = r.record(source, duration=5)  # Capture 5 seconds of audio
    with open("biometric_data/voice_data.wav", "wb") as f:
        f.write(audio_data.get_wav_data())
    print("Voice data captured and stored.")
