from socket import fromshare
from django.forms import ModelForm
from music.models import Song

class UploadSongs(ModelForm):
    class Meta:
        model = Song
        fields = ['song_file']