from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('<id_movie>', views.id_movie, name='id_movie'),
    path('<movie_title>', views.a_movie, name='a_movie'),
    path('<id_movie>', views.push_bag, name='push_bag'),

]

#r'^panel/person/(?P<person_id>[0-9]+