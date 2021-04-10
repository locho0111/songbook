import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_id = "2299de3db00442eba2d6bdb9bb9b0127"
client_secret = "6b78cccaacae4a52809b1f49ecd6c9dc"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)