import VoiceAssistent
import json

assistent = VoiceAssistent.VoiceAssistent("wake")


audio = assistent.get_audio()
assistent.speak(audio)