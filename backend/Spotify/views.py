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
    elif play_type == "queue":
        track_obj.add_to_queue(name)

    return JsonResponse(data={"response": [{"status": "success"}]}, safe=False)


def playable_devices(request):
    return JsonResponse(data={"devices": device_obj.get_all_names()}, safe=False)


def set_volume(request):
    data = json.loads(request.body)
    volume = data["volume"]

    if volume.isnumeric():
        active_device_obj.change_volume(int(volume))

    return JsonResponse(data={"response": {"status": "success"}}, safe=False)


def add_songs_to_queue(request):
    data = json.loads(request.body)

    current_track_obj.add_recomended_to_queue(
        active_device_obj.get_active_device(),
        int(data["num_to_queue"]),
    )

    return JsonResponse(data={"response": [{"status": "success"}]}, safe=False)


def current_artist(request):
    try:
        artist = current_track_obj.get_artist_name()
        return JsonResponse(data={"artist": artist}, safe=False)
    except JSONDecodeError:
        return JsonResponse(data={"artist": "None"}, safe=False)


def current_info(request):
    if active_device_obj.get_active_device() != "None":
        volume_percent = active_device_obj.get_volume()
    else:
        volume_percent = "None"

    # time.sleep(1)
    # print(active_device_obj.name)

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

    if volume < 0:
        volume = 0
    elif volume > 100:
        volume = 100

    return JsonResponse({"response": [{"volume": active_device_obj.get_volume()}]})


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
