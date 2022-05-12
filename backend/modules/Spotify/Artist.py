import tekore as tk
from tekore._model.artist import FullArtist
from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Artist:
    def __init__(self) -> None:
        pass

    def search(self, param: str) -> FullArtist:
        """Will search for artist

        Args:
            param (str): name of artist to search

        Returns:
            json: JSON containing artist information
        """
        if len(param) < 1:
            raise ValueError("Name must be at least one character long")

        (artists,) = spotify.search(
            param,
            types=("artist",),
            limit=1,
        )
        artist = artists.items[0]
        return artist

    def play(self, artist_name: str, device: str) -> None:
        """Will play artist

        Args:
            artist_name (str): Name of artist to play
            device (str, optional): name of the device you want to play on. Defaults to "MYPC".

        Raises:
            ValueError: if the artist name is less than 1 character long

        Returns:
            [None]: None
        """

        artist = self.search(artist_name)
        artist_uri = tk.to_uri("artist", artist.id)
        device_id = Device.get_id(device)
        spotify.playback_start_context(
            context_uri=artist_uri, device_id=device_id, position_ms=0
        )

        return
