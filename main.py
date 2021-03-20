import spotipy
import spotipy.oauth2 as oauth2
import configparser


def get_playlist_tracks(playlist_id):
    results = spotify.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)
# example playlist
tracks = get_playlist_tracks('0B4jhlB6QUGHzY8i3rEwTt')
for track in tracks:
    track_contents = track['track']
    track_name = track_contents['name']
    artist_contents = track_contents['artists']
    artists_name_list = list()
    for artist in artist_contents:
        artists_name_list.append(artist['name'])
    print(track_name, artists_name_list)
