import VoiceAssistent
import json

assistent = VoiceAssistent.VoiceAssistent("wake")

try:
    assistent.close_code()
except Exception as e:
    print(e)
