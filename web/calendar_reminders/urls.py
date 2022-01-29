from django.urls import path, include

urlpatterns = [
    path("spotify/", include("Spotify.urls")),
]