import speech_recognition as sr
r = sr.Recognizer()

source = sr.AudioFile('uploads/audio.wav')
with source as source_:
    r.adjust_for_ambient_noise(source_)
    audio = r.record(source_)

print(r.recognize_sphinx(audio))