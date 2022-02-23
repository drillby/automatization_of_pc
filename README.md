# Automatization of PC

Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup:

I am using Python 3.10.1, 3.8.10 and 3.9.9, so it is tested and debugged only for theese versions.
To install all the nessesary packages run <br>
`pip install -r requirements.txt`

Recomended OS is any Unix based system, Windows machines will experience not working face_recognition and there may be truble with PyAudio.

### Server hosting:

So far I am hosting a server on my PC using Django library. Soon I will be hosting a server on RaspberryPi or Synology NAS if possible.
To change Django to your local network go into web/web/setting.py and change content of ALLOWED_HOSTS

### Spotify:

- You need to set up tekore.cfg. See https://tekore.readthedocs.io/en/stable/getting_started.html, and put it in the web/web folder. For that use <br>

```python
from modules.Spotify.Spotify_auth import create_credentials

create_credentials()
```

- Also you need to set up developer account for Spotify. See https://developer.spotify.com
- Some functions may require Spotify premium account
- All of the functions are described in the web/modules/Spotify folder in each file

### Amazon Alexa:

- So far only an idea.
- Goal: Create script that will be able to control smart lights in the house using Alexa API.

### Calendar + Reminders:

- Only working on Apple services.
- All of your events and reminders must be backed up on iCloud.
- pyicloud may raise this error: Authentication required for Account. (421) <br> fix <a href="Authentication required for Account. (421)">here</a>

## IDEAS:

- Add playing on more devices at once (currently not possible because of Spotify's API)
- Redo device finding on Spotify
- Buy NFC tag to be able to start face recognition/detection script on RaspberryPi.
- Set up face recognition and start my PC on match.

## ISSUES:

- Don't know how to figure out face recognition.
