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

        with open("code_projects_location.json", "r") as f:
            self.code_projects_location = json.load(f)

        self.os = VoiceAssistent.get_running_os()

    def listen_for_wake_word(self) -> bool:
        """Will listen for wake word

        Returns:
            bool: Wake word registered
        """
        text = self.get_audio()
        if text.count(self.wake_word) > 0:
            return True
        else:
            return False

    def get_audio(self) -> str:
        """Will get audio

        Returns:
            str: str of audio
        """
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

    def speak(self, msg: str) -> None:
        """Will say given message

        Args:
            msg (str): Message to say
        """
        tts = gTTS(text=msg, lang="en", tld="ie")
        voice_file = "voice.mp3"
        tts.save(voice_file)
        playsound.playsound(voice_file)

        return

    @staticmethod
    def get_running_os() -> str:
        """Will recognize running OS

        Returns:
            int: 1=linux, 2=windows
        """
        _os = platform.system().lower()
        return _os

    def get_id_of_app(self, app: str) -> list:
        if self.os == "linux":
            return subprocess.Popen(
                f"pidof {app}", shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
                    "utf-8").split(" ")

    def get_opened_apps(self) -> str:
        """Will return a ByteString of the opened apps

        Returns:
            str: Opened apps
        """
        if self.os == "linux":
            return subprocess.Popen(
                "xlsclients", stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
        if self.os == "windows":
            return subprocess.Popen(
                "tasklist", stdout=subprocess.PIPE).communicate()[0].decode("utf-8")

    def open_code(self, path) -> None:
        subprocess.Popen(
            "code .", stdout=subprocess.PIPE, shell=True, cwd=path).communicate()[0]

        return

    def close_code(self) -> None:
        subprocess.Popen(
            f"kill {int(self.get_id_of_app('code')[-1])}", stdout=subprocess.PIPE, shell=True
        ).communicate()[0]

        return

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
