import os
import json
import requests



# Search GitHub's repositories for requests
response = requests.get(
    'https://api.themoviedb.org/3/discover/movie?api_key=fcbf9f302d5fcc8a3d775556c623b770&primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22'
)


class get_movies():
    movies = response.text
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