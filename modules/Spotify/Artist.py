import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
from tekore._model.artist import FullArtist
from modules.Spotify.Device import Device

# auth of Spotify account
conf = tk.config_from_file("tekore.cfg", return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])

# give Spotify acces to API
spotify = tk.Spotify(conf)
spotify.token = user_token


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
