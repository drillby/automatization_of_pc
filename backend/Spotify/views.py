import json
import time
from json import JSONDecodeError

import modules.Spotify.ActiveDevice
import modules.Spotify.Album
import modules.Spotify.Artist
import modules.Spotify.CurrentTrack
import modules.Spotify.Device
import modules.Spotify.Playlist
import modules.Spotify.Track
from django.http import JsonResponse
from django.shortcuts import redirect

artist_obj = modules.Spotify.Artist.Artist()
album_obj = modules.Spotify.Album.Album()
playlist_obj = modules.Spotify.Playlist.Playlist()
device_obj = modules.Spotify.Device.Device()
active_device_obj = modules.Spotify.ActiveDevice.ActiveDevice()
track_obj = modules.Spotify.Track.Track()
current_track_obj = modules.Spotify.CurrentTrack.CurrentTrack()


# Create your views here.


def start_playback(request):
    data = json.loads(request.body)
    device = data["device_name"]
    play_type = data["play_type"]
    name = data["name"]

    if device == "":
        device = active_device_obj.get_active_device()
    else:
        active_device_obj.update_active_device(device)

    if play_type == "song":
        track_obj.play(name, device)
    elif play_type == "artist":
        artist_obj.play(name, device)
    elif play_type == "album":
        album_obj.play(name, device)
    elif play_type == "playlist":
        playlist_obj.play(name, device)

    return JsonResponse(data={"response": [{"status": "success"}]}, safe=False)


def playable_devices(request):
    return JsonResponse(data={'devices': device_obj.get_all_names()}, safe=False)


def current_artist(request):
    try:
        artist = current_track_obj.get_artist_name()
        print(artist)
        return JsonResponse(data={'artist': artist}, safe=False)
    except JSONDecodeError:
        return JsonResponse(data={'artist': "None"}, safe=False)


def current_info(request):
    if active_device_obj.get_active_device() != "None":
        volume_percent = active_device_obj.get_volume()
    else:
        volume_percent = "None"

    # time.sleep(1)

    try:

        (
            playing_track,
            cover_of_track,
        ) = current_track_obj.get_name_and_cover()
        current_artist = current_track_obj.get_artist_name()
    except Exception:
        playing_track = "None"
        current_artist = ""
        cover_of_track = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/768px-Spotify_logo_without_text.svg.png"

    content = {
        "active_device": {
            "name": active_device_obj.get_active_device(),
            "volume": volume_percent,
        },
        "current_track": {
            "name": playing_track,
            "artist": current_artist,
            "cover": cover_of_track,
        },
    }

    return JsonResponse({"results": [content]})


def active_device(request):
    if active_device_obj.get_active_device() != "None":
        volume_percent = active_device_obj.get_volume()
    else:
        volume_percent = 0

    content = {
        "active_device": active_device_obj.get_active_device(),
        "volume_percent": volume_percent,
    }
    return JsonResponse({"results": [content]})


def update_volume(request):
    volume = request.POST["desired_volume"]
    active_device_obj.change_volume(volume)

    return JsonResponse(
        {"response": [{"volume": active_device_obj.get_volume()}]}
    )


def current_song(request):
    try:

        (
            playing_track,
            cover_of_track,
        ) = current_track_obj.get_name_and_cover()
    except JSONDecodeError:
        playing_track = "None"
        cover_of_track = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/768px-Spotify_logo_without_text.svg.png"

    content = {
        "name": playing_track,
        "cover": cover_of_track,
    }
    return JsonResponse({"results": [content]})


def run_spotify(request):
    device = request.POST["device"]
    text = request.POST["name"]

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
    volume = request.POST["desired_volume"]

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
