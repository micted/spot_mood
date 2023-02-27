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

print("hello")