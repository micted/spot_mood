import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import requests
import openai

# Get environment variables
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
table_name = os.environ.get("DYNAMODB_TABLE_NAME")
gsi_name = "access_token-timestamp-index"
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Create a DynamoDB client
dynamodb = boto3.client("dynamodb")



# Use the scan method to retrieve the last item in the table sorted by timestamp in descending order
response = dynamodb.scan(
TableName=table_name,
#Limit=1
)
print("this is test modificaiton so that to check my pipeline deploy smoothly   ")

items = response.get("Items")

# If the table is empty or the access token is not found, return an error response
if not items:
    print("DynamoDB table is empty")
   


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





def get_artists_from_playlist(playlist_uri):
    '''
    :param playlist_uri: Playlist to analyse
    :return: A dictionary(artist uri : artist name) of all primary artists in a playlist.
    '''
    artists = {}
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)
    for song in playlist_tracks['items']:
        if song['track']:
            print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    return artists


def list_playlist(playlist_uri):

    playlist_tracks = sp.playlist_tracks(playlist_id=playlist_uri)
    count = 0
    for song in playlist_tracks['items']:

        each_song = song['track']['name']
        count +=1
        print(each_song)
    return count


def get_lyrics(track, artist):
    endpoint = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get"
    params = {
        "apikey": api_key,
        "q_track": track,
        "q_artist": artist
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    lyrics = data.get("message", {}).get("body", {}).get("lyrics", {}).get("lyrics_body", "")
    #print(lyrics)
    return lyrics


def get_genre(track, artist):
    endpoint = "https://api.musixmatch.com/ws/1.1/track.search"
    params = {
        "apikey": api_key,
        "q_track": track,
        "q_artist": artist,
        "f_has_lyrics": 1,
        "page_size": 1
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    track_list = data.get("message", {}).get("body", {}).get("track_list", [])
    if track_list:
        track = track_list[0].get("track", {})
    else:
        track = {}
    music_genre_list = track.get("primary_genres", {}).get("music_genre_list", [])
    if music_genre_list:
        genre = music_genre_list[0].get("music_genre", {}).get("music_genre_name", "")
    else:
        genre = ""
    return genre


def liked_song(track):

    liked_tracks = []
    
    results = sp.current_user_saved_tracks()
    
    while results:

        for item in results["items"]:

            liked_tracks.append(item["track"]["name"])
        if results["next"]:
            results = sp.next(results)
        else:
            results = None
    
    if track in liked_tracks:
   
        return True
    return False
    

def analyze_mood(lyrics):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Rate the mood of the following lyrics out of 5: ' + lyrics,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # in the return message there are different answers we choose the first answer  
    message = response["choices"][0]["text"].strip()

    try:
        score = int(message.split()[0])
    except ValueError:
        score = 0
    return score


def analyze_track_mood(genre, num_plays, lyrics_mood_score, is_liked):

    genre_weights = {
        "Pop": 0.3,
        "Rock": 0.2,
        "Jazz": 0.1,
        "jazz": 0.1,
        "Hip Hop/Rap": 0.4
    }
    
    # Assign a weight to the genre based on the genre_weights dictionary
    genre_weight = genre_weights.get(genre, 0)
    #print(genre_weight)
    
    # The number of plays score is given a weight of 0.2
    num_plays_weight = 0.2*num_plays
    
    # The lyrics mood score is given a weight of 0.3
    lyrics_mood_score_weight = 0.3*lyrics_mood_score
    
    # The liked or not score is given a weight of 0.2
    is_liked_weight = 0.2 if is_liked else 0
    
    # Calculate the overall mood score
    overall_mood_score = (genre_weight + num_plays_weight + lyrics_mood_score_weight + is_liked_weight) / 4
    
    return overall_mood_score


def generate_joke(lyrics):
    model_engine = "text-davinci-002"
    prompt = "Generate a joke relatable to the following lyrics: \n" + lyrics
    
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def suggest_tracks(filtered_data,overall_mood):
    
    track = filtered_data.iloc[0]
    genre = track["Genre"]
    artist = track["Artist"]
    model_engine = "text-davinci-002"

    prompt = f"Generate a suggestion of {genre} tracks with a {overall_mood} mood by {artist} and similar {genre} artists"
    
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    suggestion = completions.choices[0].text
    
    print(suggestion)
   
    return suggestion


