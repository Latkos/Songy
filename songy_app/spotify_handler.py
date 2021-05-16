import spotipy
import spotipy.oauth2 as oauth2
import configparser
import random


class SpotifyHandler:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.cfg')
        self.client_id = self.config.get('SPOTIFY', 'CLIENT_ID')
        self.client_secret = self.config.get('SPOTIFY', 'CLIENT_SECRET')
        self.auth = oauth2.SpotifyClientCredentials(
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        self.spotify = spotipy.Spotify(client_credentials_manager=self.auth)


class Song:
    def __init__(self, name, artists):
        self.name = name
        self.artists = artists

    def __eq__(self, other):
        return self.name == other.name and self.artists == other.artists

    def __hash__(self):
        return hash(('title', self.name,
                     'author_name', tuple(self.artists)))

    def display(self):
        print(self.name, self.artists)


class SongListCreator:
    @staticmethod
    def remove_duplicated_songs(songs):
        return list(set(songs))

    @staticmethod
    def extract_songs(tracks):
        songs = list()
        for track in tracks:
            track_contents = track['track']
            track_name = track_contents['name']
            artist_contents = track_contents['artists']
            artists_name_list = list()
            for artist in artist_contents:
                artists_name_list.append(artist['name'])
            songs.append(Song(track_name, artists_name_list))
        return songs

    @staticmethod
    def get_playlist_tracks(link, spotify):
        results = spotify.playlist_items(link)
        tracks = results['items']
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])
        return tracks

    def create_song_list(self, link_list):
        # example playlist
        handler = SpotifyHandler()
        songs = list()
        for link in link_list:
            tracks = self.get_playlist_tracks(link, handler.spotify)
            songs.extend(self.extract_songs(tracks))
            random.shuffle(songs)
        songs = self.remove_duplicated_songs(songs)
        return songs
