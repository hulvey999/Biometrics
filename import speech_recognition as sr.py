import speech_recognition as sr

r = sr.Recognizer()

# Load stored voice data
with sr.AudioFile('biometric_data/voice_data.wav') as source:
    stored_audio = r.record(source)

# Capture live voice data
with sr.Microphone() as source:
    print("Say something to verify...")
    live_audio = r.record(source, duration=5)

# Compare the stored and live data
try:
    stored_text = r.recognize_google(stored_audio)
    live_text = r.recognize_google(live_audio)

    if stored_text == live_text:
        print("Voice verified successfully.")
    else:
        print("Voice verification failed.")

except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
