from tekore._model.playlist import SimplePlaylist
from .Device import Device
from .Spotify_auth import Spotify_Auth


spotify_token, spotify = Spotify_Auth()


class Playlist:
    def __init__(self):
        pass

    def search(self, playlist_name: str) -> SimplePlaylist:
        """Will search the playlist

        Args:
            playlist_name (str): Name of the playlist you want to search

        Returns:
            json: JSON of the playlist
        """
        if len(playlist_name) < 1:
            raise ValueError("Name must be at least one character long")

        (playlist,) = spotify.search(
            playlist_name,
            types=("playlist",),
            limit=1,
        )
        playlist = playlist.items[0]

        return playlist

    def play(self, playlist_name: str, device: str) -> None:
        """Will play a playlist

        Args:
            playlist_name (str): name of the playlist you want to play
            device (str, optional): name of the device you wan tot play on. Defaults to "MYPC".

        Raises:
            ValueError: if the playlist name is less than 1 character long

        Returns:
            [None]: None
        """

        playlist = self.search(playlist_name)
        device_id = Device.get_id(device)
        spotify.playback_start_context(
            context_uri=playlist.uri, device_id=device_id, position_ms=0
        )

        return
