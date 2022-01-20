import time
from flask import Flask, render_template, request, redirect
import modules
from json.decoder import JSONDecodeError


app = Flask(__name__)

artist_obj = modules.Artist()
album_obj = modules.Album()
playlist_obj = modules.Playlist()
device_obj = modules.Device()
active_device_obj = modules.ActiveDevice()
track_obj = modules.Track()
current_track_obj = modules.CurrentTrack()

devices_name = device_obj.get_all_names()
active_device = active_device_obj.update_active_device("None")


@app.route("/")
@app.route("/home")
def home():
    active_device = active_device_obj.get_active_device()

    if active_device != "None":
        volume_percent = active_device_obj.get_volume()
    else:
        volume_percent = "None"

    time.sleep(1)

    try:

        (
            playing_track,
            cover_of_track,
        ) = current_track_obj.get_name_and_cover()
    except JSONDecodeError:
        playing_track = "None"
        cover_of_track = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/768px-Spotify_logo_without_text.svg.png"

    return render_template(
        "index.html",
        num_of_devices=len(devices_name),
        devices_name=devices_name,
        active_device=active_device,
        playing_track=playing_track,
        cover_of_track=cover_of_track,
        volume_percent=volume_percent,
    )


@app.route("/run_spotify", methods=["GET", "POST"])
def result():
    output = request.form.to_dict()
    text = output["name"]
    device = output["device"]
    if device == "":
        device = active_device_obj.get_active_device()
    else:
        active_device_obj.update_active_device(device)

    text = text.split()
    text[0] = text[0].lower()

    if text[0] == "s":
        text.pop(0)
        song = " ".join(map(str, text))
        track_obj.play(song, device)

    elif text[0] == "ar":
        text.pop(0)
        artist = " ".join(map(str, text))
        artist_obj.play(artist, device)

    elif text[0] == "al":
        text.pop(0)
        album = " ".join(map(str, text))
        album_obj.play(album, device)

    elif text[0] == "p":
        text.pop(0)
        playlist = " ".join(map(str, text))
        playlist_obj.play(playlist, device)

    elif text[0] == "f" or text[0] == "q":
        text.pop(0)
        song = " ".join(map(str, text))
        track_obj.add_to_queue(song, device)

    return redirect("http://192.168.132.102:8080")


@app.route("/change_volume", methods=["GET", "POST"])
def volume():
    output = request.form.to_dict()
    volume = output["desired_volume"]

    if volume.isnumeric():
        active_device_obj.change_volume(volume)

    time.sleep(1)

    return redirect("http://192.168.132.102:8080")


@app.route("/add_recomended_songs_to_queue", methods=["GET", "POST"])
def add_to_queue():
    output = request.form.to_dict()
    number = output["num_to_queue"]
    device = output["device"]
    if device == "":
        device = active_device_obj.get_active_device()
    else:
        active_device_obj.update_active_device(device)

    if number.isnumeric():
        current_track_obj.add_recomended_to_queue(device, number)

    return redirect("http://192.168.132.102:8080")


@app.route("/wol_Paja")
def wol_Paja():
    playlist_obj.play("Hollywood Undead Mix", "Paja pokoj")
    modules.wol.wol("DC-41-A9-E2-FE-0F", "192.168.132.255")

    return "Succes"


if __name__ == "__main__":
    app.run(host="192.168.132.102", port=8080, debug=True)
