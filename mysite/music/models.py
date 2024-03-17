from django.db import models

# Create your models here.

class Song(models.Model):
    song_file = models.FileField(upload_to="songs/")

class Playlist(models.Model):
    song_no = models.ForeignKey(Song, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50)