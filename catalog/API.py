import os
import json
import requests



# Search GitHub's repositories for requests


class Url_api():
    api_url = requests.get('https://api.themoviedb.org')
    api_key = 'api_key=fcbf9f302d5fcc8a3d775556c623b770'
    discover = '/3/discover/movie?'
    theater = '&primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22'
    popular = 'sort_by=popularity.desc'
    rite = 'certification_country=US&certification=R&sort_by=vote_average.desc'
    kids = 'certification_country=US&certification.lte=G&sort_by=popularity.desc'
    year = 'primary_release_year=2010&sort_by=vote_average.desc'
    drama = 'with_genres=18&primary_release_year=2014'
    fiction = 'with_genres=878&with_cast=500&sort_by=vote_average.desc'
    comedia = 'with_genres=35&with_cast=23659&sort_by=revenue.desc'
    gend = '/genre/movie/list'

    def on_Theater(self):
        Theater = api_url+discover+api_key
        return self.Theater




def get_movies(request):
    movies = Theater
    movie_json = json.loads(movies)
    theater = []
    x = 0

    for movie in movie_json['results']:

   
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
        #genreids = movie['genre_ids']
        title =  movie['title']
        vote_average = movie['vote_average']
        overview = movie['overview']
        release_date = movie['release_date']


        theater.append({
        "model": "catalog.Movies",
        "pk":x,
        "fields": {
        'popularity': popularity,
        'vote': vote,
        'video': video,
        'poster': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'+poster,
        'TheatreId': TheatreId,
        'adult':  adult,
        'backdrop': 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'+backdrop,
        'Language': Language,
        'original_title': original_title,
        #'genreids': genreids,
        'title': title,
        'vote_average':vote_average,
        'overview': overview,
        'release_date': release_date
        }
        })

        with open('./catalog/fixtures/movie.json', 'w') as file:
            json.dump(theater, file, indent=4) 