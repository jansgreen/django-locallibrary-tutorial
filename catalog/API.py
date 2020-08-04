import json
import requests



# Search GitHub's repositories for requests
response = requests.get(
    'https://api.themoviedb.org/3/discover/movie?api_key=fcbf9f302d5fcc8a3d775556c623b770&primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22'
)


class get_movies():
    movies = response.text
    movie_json = json.loads(movies)
    print(movie_json['page'])

    for client in movie_json['results']:
        print('popularity:', client['popularity'])
        print('vote:', client['vote_count'])
        print('video:', client['video'])
        print('poster:', client['poster_path'])
        print('id:', client['id'])
        print('adult:', client['adult'])
        print('backdrop:', client['backdrop_path'])
        print('Language:', client['original_language'])
        print('genre ids:', client['genre_ids'])
        print('title:', client['title'])
        print('vote average:', client['vote_average'])
        print('overview:', client['overview'])
        print('release_date:', client['release_date'])



  

