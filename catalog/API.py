import os
import json
import requests
from django.http import HttpResponse




# Search GitHub's repositories for requests

class Url_api:
    def __init__ (self, url):
        self.url = url


    def discover(self):
        Str_Theater = []
        num = 0
        api_url = 'https://api.themoviedb.org'
        api_key = "api_key=fcbf9f302d5fcc8a3d775556c623b770"
        url_page = requests.get(str(api_url)+str(self.url)+str(api_key)).text
        total_pages = json.loads(url_page)
        pages = int(total_pages["total_pages"])
        for page in range(1, pages):
            lib = requests.get(str(api_url)+str(self.url)+str(api_key), params={'page':page}).text
            lib_movie = json.loads(lib)
            Str_Theater.append(lib_movie)
        Theater = Str_Theater
        return Theater



def get_movies(): # this functios make complete the url API
    url = "/3/discover/movie?"
    get_url = Url_api(url)
    Theater = get_url.discover()
    movie_json = Theater

    data = movie_json
    Name_data = "movie"
    set_data = mk_data(data, Name_data)
    def_data = set_data.mk_field()

class mk_data():
    def __init__(self, data, Name_data):
        self.data = data
        self.Name_data = Name_data
    
    
    def mk_field(self):
        theater=[]
        full_data = self.data
        x = 0
        for result in full_data:
            obj_movie = result["results"]
            for movie in obj_movie:
                x +=1
                popularity = movie['popularity']
                vote = movie['vote_count']
                video = movie['video']
                poster = movie['poster_path']
                TheatreId = movie['id']
                adult =  movie['adult']
                backdrop = movie['backdrop_path']
                Language = movie['original_language']
                original_title = ['original_title']
                genreids = movie['genre_ids']
                title =  movie['title']
                vote_average = movie['vote_average']
                overview = movie['overview']

                if "release_date" in movie:
                    release_date = movie['release_date']
                else:
                    release_date = "2020-01-01"
                    pass
                if int(popularity) > 0 | int(vote_average) > 0 :
                    price = round((popularity/vote_average)* 2.5, 2)
                else:
                    price = round((20/10)* 2.5, 2)


                theater.append({
                    "model": "catalog.Movies",
                    "pk":x,
                    "fields": {
                    'popularity': popularity,
                    'vote': vote,
                    'video': video,
                    'poster': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'+str(poster),
                    'TheatreId': TheatreId,
                    'adult':  adult,
                    'backdrop': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'+str(backdrop),
                    'Language': Language,
                    'original_title': original_title,
                    'genreids': genreids,
                    'title': title,
                    'vote_average':vote_average,
                    'overview': overview,
                    'release_date': release_date,
                    'price': price
                    }
                })
                url = str('./catalog/fixtures/')+str(self.Name_data)+str('.json')
                with open(url, 'w') as file:
                    json.dump(theater, file, indent=4)
            
    