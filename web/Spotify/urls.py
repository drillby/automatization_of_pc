from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("run_spotify", views.run_spotify, name="run_spotify"),
    path("change_volume", views.volume, name="change_volume"),
    path(
        "add_recomended_songs_to_queue", views.add_to_queue, name="add_songs_to_queue"
    ),
    path("live_update", views.live_update, name="live_update"),
]
