from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .spotify_handler import SongListCreator


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
    return render(request, 'game.html', {})
