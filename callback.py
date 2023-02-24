import os
import time
import boto3
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
table_name = os.environ.get("DYNAMODB_TABLE_NAME")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)
scope = "user-library-read user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-recently-played"

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope,open_browser=False)

def lambda_handler(event, context):
    print("Event received: ", event)
    
    auth_token = event.get("queryStringParameters", {}).get("code", None)
    print("Authorization token: ", auth_token)
    
    token_info = sp_oauth.get_access_token(auth_token)
    access_token = token_info["access_token"]
    print("Access token: ", access_token)
    
    timestamp = int(time.time()) + 86400
    
    table.put_item(Item={"access_token": access_token, "timestamp": timestamp})
    print("Access token stored in DynamoDB")
    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"message": "Access token stored successfully"})
    }
    print("Response: ", response)
    
    return response
