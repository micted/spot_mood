import os
import boto3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import datetime
import csv
from tools.playlists import get_lyrics, get_genre, analyze_mood, analyze_track_mood, liked_song, generate_joke, suggest_tracks
from tools.mood_analysis import overall_mood
from config.filter_tracks import filtered_for_suggestion
import openai 
import random
from collections import Counter


# Get environment variables
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
table_name = os.environ.get("DYNAMODB_TABLE_NAME")
gsi_name = "access_token-timestamp-index"

# Create a DynamoDB client
dynamodb = boto3.client("dynamodb")


# Use the scan method to retrieve the last item in the table sorted by timestamp in descending order
response = dynamodb.scan(TableName=table_name)
print("hi")
items = response.get("Items")

# If the table is empty or the access token is not found, return an error response
if not items:
    print("DynamoDB table is empty")
    error = {"statusCode": 500, "body": {"error": "access_token item not found in DynamoDB table"}}
    print(error)

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

def track_counter():
    li = []
    for item in results["items"]:
        track = item["track"]["name"]
        li.append(track)
    return li
c = Counter(track_counter())

def gather_data(results,c):
    
    with open("/tmp/recently_played.csv", "w", newline="") as csvfile:

        fieldnames = ["Track Name", "Artist", "Album", "Timestamp","Count","Genre","Lyrics Mood","Liked"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in results["items"]:

            track = item["track"]
            ly = get_lyrics(track["name"],track["artists"][0]["name"])
            writer.writerow({
                "Track Name": track["name"],
                "Artist": track["artists"][0]["name"],
                "Album": track["album"]["name"],
                "Timestamp": item["played_at"],
                "Count": c[track["name"]],
                "Genre": get_genre(track["name"],track["artists"][0]["name"]),
                "Lyrics Mood": analyze_mood(ly),
                "Liked": liked_song(track["name"])
            })

    s3_resource = boto3.resource('s3')
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/recently_played.csv'
    s3_resource.Object('spotify-mood-analyzer-spotmood', filename).upload_file("/tmp/recently_played.csv", ExtraArgs={'ACL': 'public-read'})
    url = f'https://s3.amazonaws.com/spotify-mood-analyzer-spotmood/{filename}'

    return url


def overall_mood_analyzer_suggester(results,c,filtered_data):

    final_mood_score = []
    track_names = []

    for item in results["items"]:

        track = item["track"]
        track_names.append([track["name"],track["artists"][0]["name"]])
        ly = get_lyrics(track["name"],track["artists"][0]["name"])
        num_plays = c[track["name"]],
        Genre = get_genre(track["name"],track["artists"][0]["name"]),
        lyrics_mood_score = analyze_mood(ly),
        is_liked = liked_song(track["name"]),
        final_score = analyze_track_mood(Genre[0], num_plays[0], lyrics_mood_score[0], is_liked[0])
        final_mood_score.append(final_score)


    #return final_mood_score
    track_array_len = len(track_names)
    random_index = random.randint(0,track_array_len-1)
    lyrics_for_joke = get_lyrics(track_names[random_index][0],track_names[random_index][1])


    overall_mood_state = overall_mood(final_mood_score)

    if overall_mood_state == "sad" or overall_mood_state == "very sad":

            print("Ohh you sad...ok let me tell you some Joke: \n", generate_joke(lyrics_for_joke))
    elif overall_mood_state == "happy" or overall_mood_state == "very happy":
        print("Track Recommendations: ", suggest_tracks(filtered_data,overall_mood_state))
    else:
        print("You seem to be in a neutral mood.")


def lambda_handler(event, context):

    url = gather_data(results, c)

    filtered_data = filtered_for_suggestion(url)

    message = overall_mood_analyzer_suggester(results, c, filtered_data)

    print(message)