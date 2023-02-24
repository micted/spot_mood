import os
import boto3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import datetime

# Get environment variables
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
table_name = os.environ.get("DYNAMODB_TABLE_NAME")
gsi_name = "access_token-timestamp-index"

# Create a DynamoDB client
dynamodb = boto3.client("dynamodb")
#table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    # Use the scan method to retrieve the last item in the table sorted by timestamp in descending order
    response = dynamodb.scan(
    TableName=table_name,
    #Limit=1
    )

    items = response.get("Items")

    # If the table is empty or the access token is not found, return an error response
    if not items:
        print("DynamoDB table is empty")
        return {"statusCode": 500, "body": {"error": "access_token item not found in DynamoDB table"}}

    print(items)
    #access_token_value = last_item['S']
    latest_timestamp = 0
    
    for i in range(len(items)):
        if int(items[i]["timestamp"]["N"]) > latest_timestamp:
            latest_timestamp = int(items[i]["timestamp"]["N"])
            latest_token = items[i]["access_token"]["S"]
    access_token_value = latest_token

    print(access_token_value)

    sp = spotipy.Spotify(auth=access_token_value)

    results = sp.current_user_recently_played(limit=5)
    now = datetime.datetime.now()
    recently_played = [track for track in results["items"] if (now - datetime.datetime.strptime(track["played_at"], "%Y-%m-%dT%H:%M:%S.%fZ")).total_seconds() / 3600 <= 24]
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"recently_played": recently_played})
    }
