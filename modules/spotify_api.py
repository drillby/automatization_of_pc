import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
import json
import requests
from tekore._model.artist import FullArtist
from tekore._model.playlist import SimplePlaylist
from tekore._model.track import FullTrack
from tekore._model.album import SimpleAlbumPaging
from json.decoder import JSONDecodeError

conf = tk.config_from_file("tekore.cfg", return_refresh=True)  # autorizace Spotify účtu
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(conf)  # vytvoření Spotify objektu
spotify.token = user_token  # přidělení uživatelského tokenu objektu spotify

DEVICE_NAME = ""
"""
Workaround for API call
API call is too slow for immediately showing device name on screen
"""


def search_artist(param: str) -> FullArtist:
    """Will search for artist

    Args:
        param (str): name of artist to search

    Returns:
        json: JSON containing artist information
    """
    (artists,) = spotify.search(
        param,
        types=("artist",),
        limit=1,
    )
    artist = artists.items[0]
    return artist


def play_artist(artist_name: str, device: str = "MYPC") -> None:
    """Will play artist

    Args:
        artist_name (str): Name of artist to play
        device (str, optional): name of the device you want to play on. Defaults to "MYPC".

    Raises:
        ValueError: if the artist name is less than 1 character long

    Returns:
        [None]: None
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


def search_album(param: str) -> SimpleAlbumPaging:
    """Will search for an album

    Args:
        param (str): name of album to search

    Returns:
        json: JSON containing information about the search result
    """
    (albums,) = spotify.search(
        param,
        types=("album",),
        limit=1,
    )

    return albums


def play_album(album_name: str, device: str = "MYPC") -> None:
    """Will play an album

    Args:
        album_name (str): Name of the album to play
        device (str, optional): Name of the device you want to play on. Defaults to "MYPC".

    Raises:
        ValueError: if the album name is less than 1 character long

    Returns:
        None: None
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
    """Will return a list of devices connected to the LAN

    Returns:
        json: JSON containing information about the devices
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
    """Will return an id of specific device

    Args:
        device_name (str, optional): Name of the device you want to get the id. Defaults to "MYPC".

    Returns:
        int: ID of the device
    """
    for device in get_devices()["devices"]:
        if device["name"] == device_name:
            return device["id"]

    return


def get_all_devices_name() -> list:
    """Will return a list of all connected devices

    Returns:
        list: List containing names of the devices
    """
    devices_name = []
    devices = get_devices()["devices"]
    for device in devices:
        devices_name.append(device["name"])

    return devices_name


def search_track(param: str) -> FullTrack:
    """Will search for track

    Args:
        param (str): Name of the track you want to search

    Returns:
        json: JSON containing information about the track
    """
    (tracks,) = spotify.search(
        param,
        types=("track",),
        limit=1,
    )
    track = tracks.items[0]
    return track


def play_track(track_name: str, device: str = "MYPC") -> None:
    """Will play the specific track

    Args:
        track_name (str): Name of the track you want to play
        device (str, optional): Name of the device to play on. Defaults to "MYPC".

    Raises:
        ValueError: if the track name is less than 1 character long

    Returns:
        None: None
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
    """Will shuffle the tracks

    Args:
        boolean (bool, optional): True = shuffle, False = dont shuffle. Defaults to True.
        device (str, optional): Name of the device to shuffle tracks from. Defaults to "MYPC".
    """
    device_id = get_device_id(device)
    spotify.playback_shuffle(boolean, device_id=device_id)

    return


def add_song_to_queue(track_name: str, device: str = "MYPC") -> None:
    """Will add a song to the queue

    Args:
        track_name (str): Name of the track to add to the queue
        device (str, optional): Name of the device you want to add to queue from. Defaults to "MYPC".
    """
    track = search_track(track_name)
    track_uri = tk.to_uri("track", track.id)
    device_id = get_device_id(device)
    spotify.playback_queue_add(uri=track_uri, device_id=device_id)

    return


def search_playlist(playlist_name: str) -> SimplePlaylist:
    """Will search the playlist

    Args:
        playlist_name (str): Name of the playlist you want to search

    Returns:
        json: JSON of the playlist
    """
    (playlist,) = spotify.search(
        playlist_name,
        types=("playlist",),
        limit=1,
    )
    playlist = playlist.items[0]

    return playlist


def play_playlist(playlist_name: str, device: str = "MYPC") -> None:
    """Will play a playlist

    Args:
        playlist_name (str): name of the playlist you want to play
        device (str, optional): name of the device you wan tot play on. Defaults to "MYPC".

    Raises:
        ValueError: if the playlist name is less than 1 character long

    Returns:
        [None]: None
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


def get_device_volume(device_name: str = "MYPC") -> int | None:
    """Will return the current device volume

    Args:
        device_name (str, optional): Name of the device you want to get volume from. Defaults to "MYPC".

    Returns:
        int: Persentage volume
    """
    for device in get_devices()["devices"]:
        if device["name"] == device_name:
            return device["volume_percent"]

    return


def change_volume(volume: int, device: str = "MYPC") -> None:
    """Will change the volume of the device

    Args:
        volume (int): Defired volume of the device
        device (str, optional): Name of the device you want to change volume on. Defaults to "MYPC".
    """
    device_id = get_device_id(device)
    spotify.playback_volume(volume, device_id)

    return


def get_active_device() -> str | None:
    """Will return the active devices

    Returns:
        str: Name of the device that is currently active
    """
    for device in get_devices()["devices"]:
        if device["is_active"]:
            return device["name"]

    return


def set_active_device(device: str = "MYPC") -> None:
    """Will set the active device

    Args:
        device (str, optional): Name of the device you want to set to active. Defaults to "MYPC".
    """
    for device in get_devices()["devices"]:
        if device["name"] == device:
            device["is_active"] = True

    return


def get_currently_playing_track_json() -> json | None:
    """Will return the currently playing track json

    Returns:
        json: JSON containing the currently playing track information
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


def get_name_and_cover_of_currently_playing_track() -> tuple[str, str]:
    """Will return the name and cover of the currently playing track

    Returns:
        tuple: (name of the currently playing track, cover of the currently playing track)
    """

    json = get_currently_playing_track_json()
    return (json["item"]["name"], json["item"]["album"]["images"][0]["url"])


def get_ids_for_recomendation() -> tuple[str, list[str]]:
    """Will return the tuple containing the ids recommended songs based on the currently playing

    Returns:
        tuple: IDs of the recommended songs
    """
    artists_id = []
    json = get_currently_playing_track_json()
    for i in range(0, len(json["item"]["artists"])):
        artists_id.append(json["item"]["artists"][i]["id"])
    return (artists_id, [json["item"]["id"]])


def get_uris_recomended_songs(num_of_songs: int = 20) -> list[str]:
    """Will conver the tuple of recommended ids to uris

    Args:
        num_of_songs (int, optional): Number of songs you want to convert. Defaults to 20.

    Raises:
        ValueError: If the number of songs you want to convert is greater than 100

    Returns:
        list: Contains the recommended uris
    """
    if int(num_of_songs) > 100:
        raise ValueError("Number of recommended songs cant be more than 100")

    artists_ids, song_id = get_ids_for_recomendation()
    recom = spotify.recommendations(
        artist_ids=artists_ids, track_ids=song_id, limit=num_of_songs
    ).tracks

    return [t.uri for t in recom]


def add_recomended_songs_to_queue(device: str = "MYPC", num_of_songs: int = 20) -> None:
    """Will add recommended song to the queue

    Args:
        device (str, optional): Name of the device you want to add songs to queue to. Defaults to "MYPC".
        num_of_songs (int, optional): Number of devices you want to add to queue. Defaults to 20.
    """
    uris = get_uris_recomended_songs(num_of_songs)
    device_id = get_device_id(device)
    for uri in range(len(uris)):
        spotify.playback_queue_add(uri=uris[uri], device_id=device_id)

    return
