import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
from tekore._model.album import SimpleAlbumPaging
from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Album:
    def __init__(self):
        pass

    def search(self, param: str) -> SimpleAlbumPaging:
        """Will search for an album

        Args:
            param (str): name of album to search

        Returns:
            json: JSON containing information about the search result
        """
        if len(param) < 1:
            raise ValueError("Name must be at least one character long")

        (albums,) = spotify.search(
            param,
            types=("album",),
            limit=1,
        )

        return albums

    def play(self, album_name: str, *device: str) -> None:
        """Will play an album

        Args:
            album_name (str): Name of the album to play
            device (str, optional): Name of the device you want to play on. Defaults to "MYPC".

        Raises:
            ValueError: if the album name is less than 1 character long

        Returns:
            None: None
        """

        album = self.search(album_name)
        album_uri = tk.to_uri("album", album.items[0].id)
        device_id = Device.get_id(device)
        spotify.playback_start_context(
            context_uri=album_uri, device_id=device_id, position_ms=0
        )
        return
