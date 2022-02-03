import wake_on_lan
import face_recognition_
import json

with open("wol_adresses.json") as file:
    data = json.load(file)

if face_recognition_.recognize():
    wake_on_lan.wol(data["macs"][0], data["broadcast_ip"])
