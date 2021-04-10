import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import requests
import json

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

client_id = "2299de3db00442eba2d6bdb9bb9b0127"
client_secret = "6b78cccaacae4a52809b1f49ecd6c9dc"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist= 'Moses Sumney'
track= 'Lonely World'

items = sp.search(q='artist:' + artist + ' track:' + track, limit=1, type='track')

track_info = items['tracks']['items']
song_uri = track_info[0]['uri']

#print(song_uri)
#print(sp.track('6B37flHSlwkx7Hzm2WZ8VA'))
#print(sp.audio_features('6B37flHSlwkx7Hzm2WZ8VA'))

print(json.dumps(song_uri, indent= 4))
print(getTrackFeatures(song_uri))


