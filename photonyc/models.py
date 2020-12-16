from django.db import models
from django.urls import reverse


class Collection(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=200)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='photos')
    date = models.CharField(max_length=100, )
    title = models.CharField(max_length=100)
    photo_url = models.TextField()
    location = models.CharField(max_length=100)
    # type = models.models.CharField(max_length=50)

    def __str__(self):
        return self.title


