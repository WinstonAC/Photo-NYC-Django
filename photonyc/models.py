from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo_url = models.TextField()
    loaction= models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.date

# class Song(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
#     title = models.CharField(max_length=100, default='no song title')
#     album = models.CharField(max_length=100, default='no album title')
#     preview_url = models.CharField(max_length=200, null=True)
    
    # def get_absolute_url(self):
    #     return reverse('song_detail', kwargs={'pk': self.pk})