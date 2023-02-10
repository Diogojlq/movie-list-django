from django.urls import path,include
from .views import MovieListView,MovieDeleteView,MovieUpdateView,MovieCreateView
from django.conf.urls.static import static
from . import forms
from . import views

urlpatterns = [
    path('',MovieListView.as_view(),name='movie_list'),
    path('movie_form',MovieCreateView.as_view(),name='movie_form'),
    path('movie_delete/<int:pk>',MovieDeleteView.as_view(),name='movie_delete'),
    path('update_movie/<int:pk>',MovieUpdateView.as_view(),name='update_movie'),
]
