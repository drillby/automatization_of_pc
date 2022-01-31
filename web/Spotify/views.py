from json import JSONDecodeError
import time
from django.shortcuts import redirect, render
from django.http import JsonResponse
import modules.Spotify.Artist
import modules.Spotify.Album
import modules.Spotify.Playlist
import modules.Spotify.Device
import modules.Spotify.ActiveDevice
import modules.Spotify.Track
import modules.Spotify.CurrentTrack


artist_obj = modules.Spotify.Artist.Artist()
album_obj = modules.Spotify.Album.Album()
playlist_obj = modules.Spotify.Playlist.Playlist()
device_obj = modules.Spotify.Device.Device()
active_device_obj = modules.Spotify.ActiveDevice.ActiveDevice()
track_obj = modules.Spotify.Track.Track()
current_track_obj = modules.Spotify.CurrentTrack.CurrentTrack()

devices_name = device_obj.get_all_names()
active_device = active_device_obj.update_active_device("None")

# Create your views here.


def index(request):
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

    content = {
        "num_of_devices": len(devices_name),
        "devices_name": devices_name,
        "active_device": active_device,
        "playing_track": playing_track,
        "cover_of_track": cover_of_track,
        "volume_percent": volume_percent,
    }
    return render(request, "Spotify/index.html", context=content)


def run_spotify(request):
    device = request.GET["device"]
    text = request.GET["name"]

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

    return redirect("/spotify/index")
    # return redirect("ulr {{urls/index}}")


def volume(request):
    volume = request.GET["desired_volume"]

    if volume.isnumeric():
        active_device_obj.change_volume(volume)

    time.sleep(1)

    return redirect("/spotify/index")


def add_to_queue(request):
    number = request.GET["num_to_queue"]
    device = request.GET["device"]

    if number.isnumeric():
        current_track_obj.add_recomended_to_queue(device, number)

    return redirect("/spotify/index")


def live_update(request):
    name, img = current_track_obj.get_name_and_cover()
    return JsonResponse(data={'name': name, 'cover': img}, safe=False)
