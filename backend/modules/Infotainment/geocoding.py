from typing import Tuple

import requests

import utils


class Geocoding:
    @staticmethod
    def coord_by_city_name(city_name: str) -> Tuple[float, float]:
        """Will return the coordinates of a given city

        Args:
            city_name (str): Name of the city you want to search

        Returns:
            Tuple[float, float]: lat, lon of the given city
        """
        api_key = utils.parse_cfg_file("OpenWeather_API_key.cfg")[
            "DEFAULT"]["api_key"]
        url = "http://api.openweathermap.org/geo/1.0/direct"

        querystring = {"q": f"{str(city_name)}", "appid": f"{api_key}"}
        headers = {'user-agent': 'vscode-restclient'}

        response = requests.request(
            "GET", url, headers=headers, params=querystring).json()[0]

        return response["lat"], response["lon"]
