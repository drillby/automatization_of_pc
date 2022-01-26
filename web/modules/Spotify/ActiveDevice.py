from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class ActiveDevice:
    def __init__(self, name: str = "None"):
        for device in Device.get_devices()["devices"]:
            if device["is_active"]:
                self.name = device["name"]
            else:
                self.name = name

    def update_active_device(self, name) -> None:
        """Will update active device

        Returns:
            None
        """
        self.name = name
        return

    def get_active_device(self) -> str:
        """Will return active device

        Returns:
            str: Active device name
        """

        return self.name

    def get_volume(self) -> int:
        """Will return volume of an active device.

        Args:
            device_name (str, optional): Name of the device you want to get volume from. Defaults to "MYPC".

        Returns:
            int: Persentage volume
        """
        for device in Device.get_devices()["devices"]:
            if device["name"] == self.name:
                return device["volume_percent"]

        return

    def change_volume(self, volume: int) -> None:
        """Will change the volume on active device

        Args:
            volume (int): Defired volume of the device
        """

        """if volume not in range(-1, 101):
            raise ValueError("Volume must be between 0 and 100")"""

        device_name = self.name
        device_id = Device.get_id(device_name)
        spotify.playback_volume(volume, device_id)

        return
