import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import datetime
import json
import platform
import errors.custome_errors


class VoiceAssistent:
    def __init__(self, wake_word: str):
        self.wake_word = wake_word

        with open("speach_responses.json", "r") as f:
            self.speach_responses = json.load(f)

        with open("speach_key_words.json", "r") as f:
            self.key_words = json.load(f)

    def listen_for_wake_word(self) -> bool:
        text = self.get_audio()
        if text.count(self.wake_word) > 0:
            return True
        else:
            return False

    def get_audio(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                return said
            except Exception:
                err = errors.custome_errors.DidNotUnderstand.__str__(self)
                return f"Exception: {err}"

    def speak(self, msg) -> None:
        tts = gTTS(text=msg, lang="en")
        voice_file = "voice.mp3"
        tts.save(voice_file)
        playsound.playsound(voice_file)

        return

    def get_running_os(self) -> int:
        _os = platform.system().lower()
        if _os == "linux":
            return 1
        elif _os == "windows":
            return 2

    def get_opened_apps(self):
        _os = VoiceAssistent.get_running_os()
        if _os == 1:
            return subprocess.Popen("xlsclients", stdout=subprocess.PIPE).communicate()[0]
        if _os == 2:
            return subprocess.Popen("tasklist", stdout=subprocess.PIPE).communicate()[0]

    def open_code(self):
        pass

    def close_code(self):
        pass

    def open_chrome(self):
        pass

    def close_chrome(self):
        pass

    def search_on_internet(self):
        pass

    def take_note(self):
        pass

    def read_note(self):
        pass

    def read_from_calendar(self):
        pass

    def open_spotify(self):
        pass

    def close_spotify(self):
        pass

    def play_song(self):
        pass

    def play_artist(self):
        pass

    def play_album(self):
        pass

    def play_playlist(self):
        pass
