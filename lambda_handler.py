import os
import spotipy
#import openai
import datetime
from flask import Flask, jsonify, request, session, redirect
from spotipy.oauth2 import SpotifyOAuth


username = os.environ.get("SPOTIFY_USERNAME")
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
scope = "user-library-read user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-recently-played"
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)



app = Flask(__name__)

def lambda_handler(event, context):
    print("invoked")
    if event['httpMethod'] == 'GET' and event['path'] == '/':
        return home()
    elif event['httpMethod'] == 'GET' and event['path'] == '/login':
        return login()
    elif event['httpMethod'] == 'GET' and event['path'] == '/spotify/recently_played':
        return get_recently_played()
    elif event['httpMethod'] == 'GET' and event['path'] == '/callback/':
        return callback()
    else:
        return {
            'statusCode': 404,
            'body': 'Not Found'
        }

def home():
    print("invoked")
    return "Welcome to my Spotify app!"

def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def callback():
    auth_token = request.args['code']
    token_info = sp_oauth.get_access_token(auth_token)
    session['oauth_token'] = token_info['access_token']
    return jsonify({'message': 'Successfully authorized!'})

def get_recently_played():
    token = session.get('oauth_token')
    if not token:
        return jsonify({'error': 'User is not authorized!'})

    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_recently_played(limit=5)
    now = datetime.datetime.now()
    recently_played = [track for track in results["items"] if (now - datetime.datetime.strptime(track["played_at"], "%Y-%m-%dT%H:%M:%S.%fZ")).total_seconds() / 3600 <= 24]
    
    return jsonify({'recently_played': recently_played})

