from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .spotify_handler import SongListCreator
from .spotify_handler import Song
import json

# def songify(request):
#     song_list_creator = SongListCreator()
#     song_list = song_list_creator.create_song_list(['https://open.spotify.com/playlist/2ArQdshMTWzfI8OZQiP7tj?si=db9b5024318b4418'])
#     for song in song_list:
#         song.display()
#     return HttpResponse('display.html')

def songy(request):
    return render(request, 'songy.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def game(request):
    if request.method=='POST':
        print(request.POST)
        time=request.POST['time']
        link=request.POST['spotify_link']
        song_list_creator=SongListCreator()
        song_list=song_list_creator.create_song_list_passable_to_JS([link])
        return render(request, 'game.html', {'titles_list':json.dumps(song_list[0]),'artists_list':json.dumps(song_list[1]),'time':time,'link':link})

