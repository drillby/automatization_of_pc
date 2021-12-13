# Automatization of PC
Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup:
I am using Python 3.10., so it is tested and debugged only for this version.

This project is coded on Windows mashine, so some changes will be needed to make it work on other platforms.

### Server hosting:
So far I am hosting a server on my PC using Flask library. Soon I will be hosting a server on RaspberryPi

### Spotify:
* You need to install the tekore package. See https://tekore.readthedocs.io/en/stable/
* Also you need to set up tekore.cfg. See https://tekore.readthedocs.io/en/stable/getting_started.html
* Some functions may require Spotify premium account

### Wake on LAN:
* So far only an idea.
* Will be using NFC tags.
* Goal: Create a script that will turn on my PC when NFC tag is read.

### Amazon Alexa:
* So far only an idea.
* Goal: Create script that will be able to control smart lights in the house.

## IDEAS:
* Shell script that will take param and return google search results with given params
* Create function for creating tekore.cfg
* Add playing on more devices at once (currently not possible because of Spotify's API configuration)

## ISSUES:
* None
