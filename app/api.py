from django.conf import settings
from rest_framework import views
from rest_framework.response import Response
from django.core.cache import cache
import requests
from .logging import logs
from .helper import jsonptojson
from .utils import get_lyrics
import json


class UserCategory(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cache = cache

    def get(self, request) -> Response:
        """
        User Catergory endpoint excepts the category the use send
        and returns a playlist of relevant songs.

        :type request: HttpRequest object
        :rtype: Response
        """
        category = request.GET['category']
        add_log = logs(self.get)
        if category:
            if category in self.cache:
                if "page" in self.cache:
                    page = self.cache.get("page")
                    self.cache.set("page", page + 1)
                else:
                    self.cache.set("page", 1)
                self.get_track_info(category)
            else:
                self.cache.set(category, [])
                self.cache.set("page", 1)

            add_log("Page count is - {} and Category Entered is - {}".
                    format(self.cache.get("page"), category))

            self.get_track_info(category)
            response = self.cache.get(category)

            return Response(response)
        return Response("Please provide category")

    def get_track_info(self, category):
        self.__get_tack(category)

    def __get_tack(self, category):
        track_url = settings.MUSIXMATCH_URL + "track.search"
        filters = "?format=jsonp&callback=callback&quorum_factor=1&page_size=2"
        page = self.cache.get("page")
        track_list = []
        counter = 0
        add_log = logs(self.get)
        try:
            track_payload = requests.get(url=track_url + filters + "&q_lyrics={}&page={}&apikey={}&page={}"
                                         .format(category, 2, settings.API_KEY, page))
            response = jsonptojson(track_payload.text)
            response = json.loads(response)

            tracks = response['message']['body']['track_list']

            for track in tracks:
                counter += 1
                lyrics = get_lyrics(track['track']['track_id'])
                track_name = track['track']['track_name']
                artist = track['track']['artist_name']

                obj = {
                        counter:
                        {
                            'track_name': track_name,
                            'artist': artist,
                            'lyrics': lyrics
                        }
                }

                track_list.append(obj)
            self.cache.set(category, track_list)

        except Exception as e:
            add_log("Caught an exception - {}".format(e))

    def __set_cache(self, category, **args):
        self.cache.set(category, args)

    def __get_cache(self, category):
        return self.cache[category]
