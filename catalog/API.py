import os
import json
import requests



# Search GitHub's repositories for requests

class Url_api:
    def __init__ (self, url):
        self.url = url


    def discover(self):
        num = 0
        api_url = 'https://api.themoviedb.org'
        api_key = "api_key=fcbf9f302d5fcc8a3d775556c623b770"
        Theater = requests.get(str(api_url)+str(self.url)+str(api_key), params={'page':1}).text
        return Theater


def get_movies(): # this functios make complete the url API
    url = "/3/discover/movie?"
    get_url = Url_api(url)
    Theater = get_url.discover()
    movie_json = json.loads(Theater)

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
        obj_movie = full_data['results']
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
            release_date = movie['release_date']
            price = round((popularity/vote_average)* 2.5, 2)


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
            
    