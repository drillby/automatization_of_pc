# Automatization of PC
Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup:
I am using Python 3.10.1, 3.8.10 and 3.9.9, so it is tested and debugged only for this version.

This project is coded on both Windows and Linux.

### Server hosting:
So far I am hosting a server on my PC using Django library. Soon I will be hosting a server on RaspberryPi or Synology NAS if possible.
To change Django to your local network go into web/web/setting.py and change content of ALLOWED_HOSTS 

### Spotify:
* You need to install the tekore package. See https://tekore.readthedocs.io/en/stable/
* You need to set up tekore.cfg. See https://tekore.readthedocs.io/en/stable/getting_started.html
* Also you need to set up developer account for Spotify. See https://developer.spotify.com
* Some functions may require Spotify premium account
### Wake on LAN:
* You need to install wakeonlan package. See https://pypi.org/project/wakeonlan/
* Also it is nessesary to enable WoL function in your BIOS and OS settings.

### Face recognition/detection:
* You need to install opencv, numpy and tensorflow.
* Also you need a webcam.
* You need to provide your photos.
* TF is currently not supported on Python 3.10+, so make sure you have lover version.

### Amazon Alexa:
* So far only an idea.
* Goal: Create script that will be able to control smart lights in the house using Alexa API.

### Calendar + Reminders:
* So far only an idea.
* Somehow get data from Google Calendar and Apple Reminders.
* Display it to the website.
* Be able to somewhat control Reminders - close them.

### Voice assistent:
* Small voice assistent that will bring together all of the functions in this project. Can be used instead of the web interface.
* Some users may run into issues with installing PyAudio library. If this happens to you, please visit this <a href='https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio'>site</a> and download version coresponding with your Python instalations

## IDEAS:
* Add playing on more devices at once (currently not possible because of Spotify's API)
* Buy NFC tag to be able to start face recognition/detection script on RaspberryPi.
* Set up face recognition and start my PC on match.
* Refactor spotify_api into classes

## ISSUES:
* Don't know how to figure out face recognition.
