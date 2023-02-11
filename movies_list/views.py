from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from movies_list.models import Movie
from .forms import MovieCreateView
from django.shortcuts import HttpResponseRedirect
from django.db import models

# Create your views here.
class MovieCreateView(CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movie_list')

class MovieListView(ListView):
    model = Movie
    template_name = 'movies_list/index.html'
    
class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movie_list')
