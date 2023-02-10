from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=30)
    note = models.CharField(max_length=30) 
    

    def __str__(self):
        return f'{self.movie_name} {self.note}'
    
    