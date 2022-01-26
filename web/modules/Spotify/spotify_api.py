import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
import json
import requests
from tekore._model.artist import FullArtist
from tekore._model.playlist import SimplePlaylist
from tekore._model.track import FullTrack
from tekore._model.album import SimpleAlbumPaging
from json.decoder import JSONDecodeError

# auth of Spotify account
conf = tk.config_from_file("tekore.cfg", return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])

# give Spotify acces to API
spotify = tk.Spotify(conf)
spotify.token = user_token

DEVICE_NAME = ""
"""
Workaround for API call
API call is too slow for immediately showing device name on screen
"""

















