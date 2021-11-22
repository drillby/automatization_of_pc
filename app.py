import spotify_api
from flask import Flask, render_template, request

devices_name = spotify_api.get_all_devices_name()

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "index.html", num_of_devices=len(devices_name), devices_name=devices_name
    )

    # Přijít na to jak vypsat hodnotu hlasitosti do html inputu
    # Přijít na to jak vypsat název zařízenní do html textu


@app.route("/run_spotify", methods=["GET", "POST"])
def result():
    output = request.form.to_dict()
    text = output["name"]
    device = output["device"]

    text = text.split()
    text[0] = text[0].lower()
    print(text[0])

    if text[0] == "s":
        text.pop(0)
        song = " ".join(map(str, text))
        print(song)
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

    return render_template(
        "index.html", num_of_devices=len(devices_name), devices_name=devices_name
    )


@app.route("/change_volume", methods=["GET", "POST"])
def volume():
    output = request.form.to_dict()
    volume = output["current_volume"]
    device = output["device"]

    if isinstance(volume, int):
        spotify_api.change_volume(volume, device)

    return render_template(
        "index.html", num_of_devices=len(devices_name), devices_name=devices_name
    )


if __name__ == "__main__":
    app.run(host="192.168.132.102", port=8080, debug=True)
