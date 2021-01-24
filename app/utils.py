import requests
from .helper import jsonptojson
import json
from django.conf import settings


def get_lyrics(track_id):
    return __get_lyrics(track_id)


def __get_lyrics(track_id):
    lyrics_url = settings.MUSIXMATCH_URL + "track.lyrics.get"
    filters = "?format=jsonp&callback=callback"

    lyrics = requests.get(url=lyrics_url + filters + '&track_id={}&apikey={}'.
                          format(track_id,settings.API_KEY))

    lyrics = jsonptojson(lyrics.text)
    lyrics = json.loads(lyrics)
    lyrics = lyrics['message']['body']['lyrics']['lyrics_body']

    return lyrics
