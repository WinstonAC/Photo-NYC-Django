from django.db import models
from django.urls import reverse


class Collection(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=200)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
# artist = collection- craete a collection class and add 1 x description text field

# Song = photo


class Photo(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='photos')
    date = models.CharField(max_length=100, )
    title = models.CharField(max_length=100)
    photo_url = models.TextField()
    loaction = models.CharField(max_length=100)

    def __str__(self):
        return self.date


# def get_absolute_url(self):
    #     return reverse('song_detail', kwargs={'pk': self.pk})


# class Collection
# class Song(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
#     title = models.CharField(max_length=100, default='no song title')
#     album = models.CharField(max_length=100, default='no album title')
#     preview_url = models.CharField(max_length=200, null=True)

    # def get_absolute_url(self):
    #     return reverse('song_detail', kwargs={'pk': self.pk})
