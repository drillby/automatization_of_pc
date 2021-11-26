import json
from json.decoder import JSONDecodeError
import tekore as tk
import requests
from tekore._model import currently_playing

conf = tk.config_from_file("tekore.cfg", return_refresh=True)  # autorizace Spotify účtu
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(conf)  # vytvoření Spotify objektu
spotify.token = user_token  # přidělení uživatelského tokenu objektu spotify

DEVICE_NAME = ""
"""
Workaround for API call
API call is too slow for immediately showing device name on screen
"""


def search_artist(param: str) -> json:
    """
    description: Will search for an artist based on the parameter
    params: param = Name of the artist
    return: JSON object containing info about the artist
    """
    (artists,) = spotify.search(
        param,
        types=("artist",),
        limit=1,
    )
    artist = artists.items[0]
    return artist


def play_artist(artist_name: str, device: str = "MYPC") -> None:
    """
    description: Will play an artist based on the parameter
    params: artist_name = Name of the artist
            device = Name of the device on which the artist will be played (default = MYPC)
    return: True
    """
    if len(artist_name) < 1:
        return ValueError("Name must be at least one character long")

    if not get_active_device():
        set_active_device()

    artist = search_artist(artist_name)
    artist_uri = tk.to_uri("artist", artist.id)
    device_id = get_device_id(device)
    spotify.playback_start_context(
        context_uri=artist_uri, device_id=device_id, position_ms=0
    )

    return


def search_album(param: str) -> json:
    """
    description: Will search for an album based on the parameter
    params: param = Name of the album
    return: Info about the album
    """
    (albums,) = spotify.search(
        param,
        types=("album",),
        limit=1,
    )

    return albums


def play_album(album_name: str, device: str = "MYPC") -> None:
    """
    description: Will play an album based on the parameter
    params: album_name = Name of the album
            device = Name of the device on which the album will be played (default = MYPC)
    return: True
    """
    if len(album_name) < 1:
        return ValueError("Name must be at least one character long")

    if not get_active_device():
        set_active_device()

    album = search_album(album_name)
    album_uri = tk.to_uri("album", album.id)
    device_id = get_device_id(device)
    spotify.playback_start_context(
        context_uri=album_uri, device_id=device_id, position_ms=0
    )
    return


def get_devices() -> json:
    """
    params: None
    return: JSON object of all conected devices to your account
    note: Devices must be on your LAN
    """
    devices = requests.get(
        "https://api.spotify.com/v1/me/player/devices",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {user_token}",
        },
    )

    return devices.json()


def get_device_id(device_name: str = "MYPC") -> int:
    """
    description: Will search for a device based on the parameter¨
    params: Name of the device
    note: Device must be on your LAN
    return: ID of the device
    """
    for device in get_devices()["devices"]:
        if device["name"] == device_name:
            return device["id"]

    return


def get_all_devices_name() -> list:
    devices_name = []
    devices = get_devices()["devices"]
    for device in devices:
        devices_name.append(device["name"])

    return devices_name


def search_track(param: str) -> json:
    """
    description: Will search for a track based on the parameter
    params: Name of the track
    return: Info about the track
    """
    (tracks,) = spotify.search(
        param,
        types=("track",),
        limit=1,
    )
    track = tracks.items[0]
    return track


def play_track(track_name: str, device: str = "MYPC") -> None:
    """
    description: Will play a track based on the parameter
    params: track_name = Name of the track you want to start playing
            device = Name of the device you want to play the track on (default = MYPC)
    return: None
    """
    if len(track_name) < 1:
        return ValueError("Name must be at least one character long")

    if not get_active_device():
        set_active_device()

    track = search_track(track_name)
    device_id = get_device_id(device)
    spotify.playback_start_tracks([track.id], device_id=device_id, position_ms=0)
    return


def shuffle_tracks(boolean: bool = True, device: str = "MYPC") -> None:
    """
    description: Will shuffle the tracks
    params: boolean = Whether or not to shuffle
            device = Name of the device you want to shuffle the tracks on (default = MYPC)
    note: True = shuffle, False = not shuffle
    return: None
    """
    device_id = get_device_id(device)
    spotify.playback_shuffle(boolean, device_id=device_id)

    return


def add_song_to_queue(track_name: str, device: str = "MYPC") -> None:
    """
    description: Will add a track to your Spotify queue
    params: track_name = Name of the album you want to add to the queue
            device = Name of the device where you want to add the track to the queue (default = MYPC)
    return: True
    """
    track = search_track(track_name)
    track_uri = tk.to_uri("track", track.id)
    device_id = get_device_id(device)
    spotify.playback_queue_add(uri=track_uri, device_id=device_id)

    return


def add_album_to_queue(album_name: str, device: str = "MYPC") -> None:
    """
    description: Will add a track to your Spotify queue
    params: track_name = Name of the album you want to add to the queue
            device = Name of the device where you want to add the track to the queue (default = MYPC)
    return: True
    """
    album = search_album(album_name)
    spotify.album_tracks
    """album_uri = tk.to_uri("track", album.id)
    device_id = get_device_id(device)
    spotify.playback_queue_add(uri=album_uri, device_id=device_id)"""

    return album


def search_playlist(playlist_name: str) -> json:
    """
    description: Will search for a playlist from your Spotify library based on the parameter
    params: playlist_name = The name of the playlist you want to play
    return: Info about the playlist
    """
    (playlist,) = spotify.search(
        playlist_name,
        types=("playlist",),
        limit=1,
    )
    playlist = playlist.items[0]

    return playlist


def play_playlist(playlist_name: str, device: str = "MYPC") -> None:
    """
    description: Will play a playlist from your Spotify library based on the parameter
    params: playlist_name = The name of the playlist you want to play
            device = Name of the device you want to play the playlist on (default = MYPC)
    return: True
    """
    if len(playlist_name) < 1:
        return ValueError("Name must be at least one character long")

    if not get_active_device():
        set_active_device()

    playlist = search_playlist(playlist_name)
    device_id = get_device_id(device)
    spotify.playback_start_context(
        context_uri=playlist.uri, device_id=device_id, position_ms=0
    )

    return


def get_device_volume(device_name: str = "MYPC") -> int:
    """
    description: Will search for a device based on the parameter¨
    params: Name of the device
    note: Device must be on your LAN
    return: ID of the device
    """
    for device in get_devices()["devices"]:
        if device["name"] == device_name:
            return device["volume_percent"]

    return


def change_volume(volume: int, device: str = "MYPC") -> None:
    """
    Will set the volume of currently playing device
    params: volume - desired volume (1-100)
            device - Name of the device
    return: None
    """
    device_id = get_device_id(device)
    spotify.playback_volume(volume, device_id)

    return


def get_active_device() -> str:
    """
    Will return active device
    params: None
    return: Name of the active devicee
    """
    for device in get_devices()["devices"]:
        if device["is_active"]:
            return device["name"]

    return


def set_active_device(device: str = "MYPC") -> None:
    """
    Will set the active device
    params: device - Name of the device (default = MYPC)
    return: None
    """
    for device in get_devices()["devices"]:
        if device["name"] == device:
            device["is_active"] = True

    return


def get_currently_playing_track_json() -> json:
    """
    Will return json of currently playing track
    params: None
    return: json of currently playing track
    """
    try:
        track_info = requests.get(
            "https://api.spotify.com/v1/me/player/currently-playing",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {user_token}",
            },
        )

        return track_info.json()
    except JSONDecodeError:
        return


def get_name_and_cover_of_currently_playing_track() -> tuple:
    """
    Will return the currently playing track
    params: None
    return: Name of the currently playing track
    """

    json = get_currently_playing_track_json()
    return (json["item"]["name"], json["item"]["album"]["images"][0]["url"])


def get_ids_for_recomendation() -> tuple:
    """
    Will return the currently playing track id
    params: None
    return: Id of the currently playing
    """
    artists_id = []
    json = get_currently_playing_track_json()
    for i in range(0, len(json["item"]["artists"])):
        artists_id.append(json["item"]["artists"][i]["id"])
    return (artists_id, [json["item"]["id"]])


def get_uris_recomended_songs(num_of_songs: int = 20) -> list:
    """
    Will return list of songs based on the currently playing track
    params: number of songs to return
    return: list of songs based on the currently playing track
    """
    artists_ids, song_id = get_ids_for_recomendation()
    recom = spotify.recommendations(
        artist_ids=artists_ids, track_ids=song_id, limit=num_of_songs
    ).tracks

    return [t.uri for t in recom]


def add_recomended_songs_to_queue(device: str = "MYPC") -> None:
    """
    Will add more tracks to the queue
    params: device - Name of the device
    return: None
    """
    uris = get_uris_recomended_songs()
    device_id = get_device_id(device)
    for uri in range(len(uris)):
        spotify.playback_queue_add(uri=uris[uri], device_id=device_id)


# Možnost úpravy počtu písniček do queue
