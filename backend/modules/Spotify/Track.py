import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
from tekore._model.track import FullTrack
from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Track:
    def __init__(self):
        pass

    def search(self, param: str) -> FullTrack:
        """Will search for track

        Args:
            param (str): Name of the track you want to search

        Returns:
            json: JSON containing information about the track
        """
        if len(param) < 1:
            raise ValueError("Name must be at least one character long")

        (tracks,) = spotify.search(
            param,
            types=("track",),
            limit=1,
        )
        track = tracks.items[0]
        return track

    def play(self, track_name: str, device: str) -> None:
        """Will play the specific track

        Args:
            track_name (str): Name of the track you want to play
            device (str, optional): Name of the device to play on. Defaults to "MYPC".

        Raises:
            ValueError: if the track name is less than 1 character long

        Returns:
            None: None
        """

        track = self.search(track_name)
        device_id = Device.get_id(device)
        spotify.playback_start_tracks([track.id], device_id=device_id, position_ms=0)
        return

    def shuffle(self, boolean: bool = True) -> None:
        """Will shuffle the tracks

        Args:
            boolean (bool, optional): True = shuffle, False = don't shuffle. Defaults to True.
        """

        spotify.playback_shuffle(boolean)

        return

    def add_to_queue(self, track_name: str) -> None:
        """Will add a song to the queue

        Args:
            track_name (str): Name of the track to add to the queue.
        """

        track = self.search(track_name)
        track_uri = tk.to_uri("track", track.id)
        spotify.playback_queue_add(uri=track_uri)

        return
