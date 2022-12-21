from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='anasayfa'),
    path("home", views.home),
    path("movies", views.movies, name='filmler'),
    path("movies/<int:id>", views.moviesdetails,name='filmdetay'),
    path("error", views.error,name = 'error'),
]