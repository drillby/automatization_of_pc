# Automatization of PC

Author: Pavel Podrazký

This project contains some ideas how to automate my work on PC.

## Instalation and setup:

I am using Python 3.8.10, so it is tested and debugged only for this versions.
To install all the nessesary packages run <br>

```python
pip install -r requirements.txt
```

**If you plan to put this web server into production you need to to this:**

You need to get youself a <a href="https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django">secret key</a> and put it into web/web/django_secret_key.cfg formated like this

```conf
[DEFAULT]
SECRET_KEY = "your_secret_key"
```

and add this code to web/settings.py

```python
parser = configparser.ConfigParser()
SECRET_KEY = parser.read("django_secret_key.cfg", "SECRET_KEY")
```

Since I will be using this server only on LAN I will expose my secret key, but it is not recomended.

## Server hosting:

So far I am hosting a server on my PC using Django library. Soon I will be hosting a server on RaspberryPi or Synology NAS if possible.
To change Django to your local network go into web/web/setting.py and change content of ALLOWED_HOSTS from localhost to some of your LAN IP
