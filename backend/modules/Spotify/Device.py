import json
import requests
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Device:
    def __init__(self):
        pass

    @classmethod
    def get_devices(self) -> json:
        """Will return a list of devices connected to the LAN

        Returns:
            json: JSON containing information about the devices
        """
        devices = requests.get(
            "https://api.spotify.com/v1/me/player/devices",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {spotify_token}",
            },
        )

        return devices.json()

    @classmethod
    def get_id(self, device_name: str) -> int:
        """Will return an id of specific device

        Args:
            device_name (str, optional): Name of the device you want to get the id. Defaults to "MYPC".

        Returns:
            int: ID of the device
        """

        for device in self.get_devices()["devices"]:
            if device["name"] == device_name:
                return device["id"]

        return

    def get_all_names(self) -> list:
        """Will return a list of all connected devices

        Returns:
            list: List containing names of the devices
        """
        return [device["name"] for device in self.get_devices()["devices"]]
