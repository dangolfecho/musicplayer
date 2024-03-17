from django.shortcuts import render, redirect
from .models import *
from .forms import UploadSongs
# Create your views here.

def mainpage(request):
    songs = Song.objects.all()
    context = {
        "songs_list": songs
    }
    return render(request, 'music/index.html', context)

def addSong(request):
    form = UploadSongs(request.POST, request.FILES)
    index = len(Song.objects.all())
    if(form.is_valid()):
        index += 1
        song = Song(song_file=request.FILES['song_file'])
        song.save()
    else:
        print("Error!")
    return redirect('mainpage')

def playSong(request):
    song_file = request.POST.get('song_file')
    songs = Song.objects.all()
    obj = Song.objects.get(song_file=song_file)
    path = obj.song_file.url
    print(path)
    context = {
        "songs_list": songs,
        "song": path
    }
    return render(request, 'music/index.html', context)