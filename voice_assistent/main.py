import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import datetime


def speak(text):
    tts = gTTS(text=text, lang="cs")
    file = "voice.mp3"
    tts.save(file)
    playsound.playsound(file)


# speak('Toto je test')


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            return said
        except Exception:
            return f"Exception: {str(Exception)}"


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


WAKE = 'wake up'

while True:
    text = get_audio()
    if text.count(WAKE) > 0:
        speak("Jsem připraven")
        #text = get_audio()
