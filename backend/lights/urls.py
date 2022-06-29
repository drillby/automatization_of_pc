from django.urls import path
from . import views


urls = [
    path("status_all", views.get_status_all, name="all devices status")
]
