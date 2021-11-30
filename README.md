# Automatization of PC
Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup
You will need Python 3.10+. I'm using structural pattern matching, which is available only from Python 3.10

The server is dynamically getting all of the speakers, but if you want to add new, you have to restart the server.

Spotify:
* You need to install the tekore package. See https://tekore.readthedocs.io/en/stable/
* Also you need to set up tekore.cfg. See https://tekore.readthedocs.io/en/stable/getting_started.html
* For web server it self I am using the Flask package. 

## IDEAS:
* Shell script that will run local server for Spotify and will open wanted web page
* Shell script that will take param and return google search results with given params
* Create function for creating tekore.cfg

## ISSUES:
* Fix adding albums to queue
