from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("addSong", views.addSong, name='addsong'),
    path("playSong", views.playSong, name='playsong')
]
