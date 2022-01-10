# Automatization of PC
Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup:
I am using Python 3.10.1, so it is tested and debugged only for this version.

This project is coded on a Windows mashine, so some changes may be needed to make it work on other platforms.

### Server hosting:
So far I am hosting a server on my PC using Flask library. Soon I will be hosting a server on RaspberryPi or Synology NAS if possible

### Spotify:
* You need to install the tekore package. See https://tekore.readthedocs.io/en/stable/
* You need to set up tekore.cfg. See https://tekore.readthedocs.io/en/stable/getting_started.html
* Also you need to set up developer account for Spotify. See https://developer.spotify.com
* Some functions may require Spotify premium account

### Wake on LAN:
* You need to install wakeonlan package. See https://pypi.org/project/wakeonlan/
* Also it is nessesary to enable WoL function in your BIOS and OS settings.

### Amazon Alexa:
* So far only an idea.
* Goal: Create script that will be able to control smart lights in the house using Alexa API.

## IDEAS:
* Shell script that will take param and return google search results with given params
* Create function for creating tekore.cfg
* Add playing on more devices at once (currently not possible because of Spotify's API)
* Buy NFC tag to be able to start face recognition script on RasoberryPi.
* Set up face recognition and start my PC on match.

## ISSUES:
* So far my only issue is that I am not coding on Linux. This will be fixed soon.
