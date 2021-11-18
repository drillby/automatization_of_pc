from __future__ import unicode_literals
from pytube import YouTube
import youtube_dl

yt = YouTube("https://www.youtube.com/watch?v=-S2or-zgiBI")
t = yt.streams.filter(only_audio=True)
t[0].download("Downloads")


ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=-S2or-zgiBI"])
