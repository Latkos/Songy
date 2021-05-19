from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .spotify_handler import SongListCreator
from .spotify_handler import Song
from spotipy.exceptions import SpotifyException
import json


def songy(request):
    return render(request, 'songy.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def game(request):
    if request.method == 'POST':
        print(request.POST)
        time = request.POST['time']
        link = request.POST['spotify_link']
        round_length = request.POST['round_length']
        song_list_creator = SongListCreator()
        try:
            song_list = song_list_creator.create_song_list_passable_to_JS([link])
        except SpotifyException:
            return render(request,'songy.html')
        return render(request, 'game.html',
                      {'titles_list': json.dumps(song_list[0]), 'artists_list': json.dumps(song_list[1]), 'time': time,
                       'link': link, 'round_length': round_length})
