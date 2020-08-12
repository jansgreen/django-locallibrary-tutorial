from django.urls import path

from . import views, mymovies

urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('<id_movie>', views.id_movie, name='id_movie'),
    path('<movie_title>', views.a_movie, name='a_movie'),
    path('add/<id_movie>', views.push_bag, name='push_bag'),
    #path('', mymovies.my_movies, name='my_movies'),


]

