from django import forms
from .models import Movie

class MovieCreateView(forms.Form):
    
    class Meta :
        model = Movie
        fields = '__all__'
    
   
