import json
import tekore as tk
import subprocess
import requests

conf = tk.config_from_file("tekore.cfg", return_refresh=True)  # autorizace Spotify účtu
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(conf)  # vytvoření Spotify objektu
spotify.token = user_token  # přidělení uživatelského tokenu objektu spotify


def get_top_tracks(number: int = 10) -> None:
    """
    description: Will print the top X tracks of your Spotify account
    params: number = number of top tracks you want to be printed
    note: default=10, max=50
    return: True
    """
    number = int(number)
    if number < 1:
        number = 10

    print(f"Top {number} tracks!")
    tracks = spotify.current_user_top_tracks(limit=number)
    for track in tracks.items:
        print(track.name)

    return


def get_albums(number: int = 10) -> None:
    """
    description: Will print the first X albums in your Spotify library
    params: number = number of albums you want to be printed
    note: default=10, max=50
    return: True
    """
    number = int(number)
    if number < 1:
        number = 10

    print(f"Your first {number} albums!")
    albums = spotify.saved_albums(limit=number)
    i = 1
    for album in albums.items:
        print(i, album.album.name)
        i += 1

    return


def open_spotify() -> None:
    """
    description: Will open Spotify
    params: None
    return: True
    """
    spotify_dir = "C:\\Users\\Administrátor\\AppData\\Roaming\\Spotify\\Spotify.exe"
    subprocess.call(spotify_dir)

    return


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
        print("Zadej název alba")
        return

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
    album = albums.items[0]
    return album


def play_album(album_name: str, device: str = "MYPC") -> None:
    """
    description: Will play an album based on the parameter
    params: album_name = Name of the album
            device = Name of the device on which the album will be played (default = MYPC)
    return: True
    """
    if len(album_name) < 1:
        print("Zadej název alba")
        return

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
        print("Zadej název alba")
        return

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
    return: True
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
    album_uri = tk.to_uri("track", album.id)
    device_id = get_device_id(device)
    spotify.playback_queue_add(uri=album_uri, device_id=device_id)

    return


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
        print("Zadej název alba")
        return

    playlist = search_playlist(playlist_name)
    device_id = get_device_id(device)
    spotify.playback_start_context(
        context_uri=playlist.uri, device_id=device_id, position_ms=0
    )

    return


def get_device_volume(device_name: str = "MYPC") -> int:
    """
    description: Will return the volume of currently playing device
    params: device name
    return: Volume of currently playing device in percent
    """
    pass


def change_volume(volume: int, device: str = "MYPC") -> None:
    device_id = get_device_id(device)
    spotify.playback_volume(volume, device_id)

    return
