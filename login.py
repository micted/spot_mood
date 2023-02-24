import os
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import requests

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
scope = "user-library-read user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-recently-played"
def lambda_handler(event, context):
    sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    auth_url = sp_oauth.get_authorize_url()
    response = {
        "statusCode": 302,
        "headers": {
            "Location": auth_url
        }
    }
    print(auth_url)
    return response