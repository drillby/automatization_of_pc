from django.urls import path
from . import views

urlpatterns = [
    path("current_song", views.current_song, name="current_song"),
    path("start_playback", views.start_playback, name="start_playback"),
    path("playable_devices", views.playable_devices, name="playable_devices"),
    path("current_artist", views.current_artist, name="current_artist"),
    path("active_device", views.active_device, name="active_device"),
    path("current_info", views.current_info, name="current_info"),

    path("run_spotify", views.run_spotify, name="run_spotify"),
    path("change_volume", views.volume, name="change_volume"),
    path(
        "add_recomended_songs_to_queue", views.add_to_queue, name="add_songs_to_queue"
    ),
    path("live_update", views.live_update, name="live_update"),
    path("set_volume", views.set_volume, name="set_volume"),
]
