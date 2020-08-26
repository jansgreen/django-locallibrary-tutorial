from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('<int:id_movie>', views.id_movie, name='id_movie'),
    path('<movie_title>', views.a_movie, name='a_movie'),
    path('add/<int:id_movie>', views.push_bag, name='push_bag'),
    path('delete/<int:Movies_id>', views.delete, name='delete'),
    path('bag/save_movies', views.save_movies, name='save_movies'),



]

urlpatterns += [
    #path('bag/create/', views.AuthorCreate.as_view(), name='author_create'),
    #path('bag/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    #path('bag/<int:pk>/delete/', views.AuthorDelete.as_view(), name='bag_delete'),
]

