import json
from typing import Tuple

import requests

import geocoding
import utils


class CurrentWeather:
    @staticmethod
    def get_current_weather_data(city_name: str) -> json:
        """Will return the current weather data for the given city

        Args:
            city_name (str): Name of the city you want to search

        Returns:
            json: JSON containing current weather data for the given city
        """
        lat, lon = geocoding.Geocoding.coord_by_city_name(str(city_name))
        api_key = utils.parse_cfg_file("OpenWeather_API_key.cfg")[
            "DEFAULT"]["api_key"]

        url = "http://api.openweathermap.org/data/2.5/weather"

        querystring = {"lat": f"{lat}", "lon": f"{lon}",
                       "appid": f"{api_key}", "units": "metric"}

        headers = {'user-agent': 'vscode-restclient'}

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        return response.json()

    @staticmethod
    def get_forecast_weather_data(city_name: str) -> json:
        """Will return the current weather data for the given city

        Args:
            city_name (str): Name of the city you want to search

        Returns:
            json: JSON containing current weather data for the given city
        """
        lat, lon = geocoding.Geocoding.coord_by_city_name(str(city_name))
        api_key = utils.parse_cfg_file("OpenWeather_API_key.cfg")[
            "DEFAULT"]["api_key"]

        url = "https://api.openweathermap.org/data/2.5/onecall"

        querystring = {"lat": f"{lat}", "lon": f"{lon}",
                       "appid": f"{api_key}", "units": "metric", "exclude": "current,minutely,daily,alerts"}

        headers = {'user-agent': 'vscode-restclient'}

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        return response.json()


print(CurrentWeather.get_forecast_weather_data("Žižice"))
