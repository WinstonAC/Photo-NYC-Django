from django import forms
from .models import Collection, Photo


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ('name', 'photo_url', 'description', )


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('date', 'title', 'photo_url', 'location', 'collection',)
