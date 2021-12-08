# Automatization of PC
Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup
I am using Python 3.8.10, so it is tested and debugged only for this version.

The server is dynamically getting all of the speakers, but if you want to add new, you have to restart the server.

Spotify:
* You need to install the tekore package. See https://tekore.readthedocs.io/en/stable/
* Also you need to set up tekore.cfg. See https://tekore.readthedocs.io/en/stable/getting_started.html
* For web server it self I am using the Flask package. 

## IDEAS:
* Shell script that will run local server for Spotify and will open wanted web page
* Shell script that will take param and return google search results with given params
* Create function for creating tekore.cfg
* Add playing on more devices at once (currently not possible because of Spotify's API configuration)

## ISSUES:
* None
