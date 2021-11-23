import time
import spotify_api
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

devices_name = spotify_api.get_all_devices_name()
active_device = spotify_api.get_active_device()
if not active_device:
    active_device = "None"

spotify_api.set_active_device()


@app.route("/")
@app.route("/home")
def home():
    active_device = spotify_api.get_active_device()
    if not active_device and not spotify_api.DEVICE_NAME:
        active_device = "None"

    if spotify_api.DEVICE_NAME:
        active_device = spotify_api.DEVICE_NAME

    time.sleep(1)

    try:
        (
            playing_track,
            cover_of_track,
        ) = spotify_api.get_name_and_cover_of_currently_playing_track()
    except TypeError:
        playing_track = "None"
        cover_of_track = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/768px-Spotify_logo_without_text.svg.png"

    return render_template(
        "index.html",
        num_of_devices=len(devices_name),
        devices_name=devices_name,
        active_device=active_device,
        playing_track=playing_track,
        cover_of_track=cover_of_track,
    )


@app.route("/run_spotify", methods=["GET", "POST"])
def result():
    output = request.form.to_dict()
    text = output["name"]
    device = output["device"]
    spotify_api.DEVICE_NAME = device

    text = text.split()
    text[0] = text[0].lower()

    if text[0] == "s":
        text.pop(0)
        song = " ".join(map(str, text))

        spotify_api.play_track(song, device)

    elif text[0] == "ar":
        text.pop(0)
        artist = " ".join(map(str, text))
        spotify_api.play_artist(artist, device)

    elif text[0] == "al":
        text.pop(0)
        album = " ".join(map(str, text))
        spotify_api.play_album(album, device)

    elif text[0] == "p":
        text.pop(0)
        playlist = " ".join(map(str, text))
        spotify_api.play_playlist(playlist, device)

    if text[0] == "f" or text[0] == "q":
        text.pop(0)
        song = " ".join(map(str, text))
        spotify_api.add_song_to_queue(song, device)

    return redirect("http://192.168.132.102:8080")


@app.route("/change_volume", methods=["GET", "POST"])
def volume():
    output = request.form.to_dict()
    volume = output["current_volume"]
    device = output["device"]

    if isinstance(volume, int):
        spotify_api.change_volume(volume, device)

    return redirect("http://192.168.132.102:8080")


if __name__ == "__main__":
    app.run(host="192.168.132.102", port=8080, debug=True)
