import spotipy
import spotipy.oauth2 as oauth2
import configparser


class SpotifyHandler:

    def __init__(self):
        self.read_config()
        self.get_client_data()
        self.auth = oauth2.SpotifyClientCredentials(
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        self.set_connection()

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.cfg')

    def get_client_data(self):
        self.client_id = self.config.get('SPOTIFY', 'CLIENT_ID')
        self.client_secret = self.config.get('SPOTIFY', 'CLIENT_SECRET')

    def set_connection(self):
        token = self.auth.get_access_token()
        self.spotify = spotipy.Spotify(auth=token)


def get_playlist_tracks(playlist_id, spotify):
    results = spotify.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


class Song:
    def __init__(self, name, artists):
        self.name = name
        self.artists = artists

    def display(self):
        print(self.name,self.artists)

# example playlist
handler = SpotifyHandler()
tracks = get_playlist_tracks('0B4jhlB6QUGHzY8i3rEwTt', handler.spotify)
songs = list()
for track in tracks:
    track_contents = track['track']
    track_name = track_contents['name']
    artist_contents = track_contents['artists']
    artists_name_list = list()
    for artist in artist_contents:
        artists_name_list.append(artist['name'])
    songs.append(Song(track_name, artists_name_list))

for song in songs:
    song.display()