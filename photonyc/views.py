from .models import Collection, Photo
from django.shortcuts import render, redirect
from .forms import CollectionForm, PhotoForm
from django.views import View
from rest_framework import generics
from .serializers import CollectionSerializer, PhotoSerializer


class CollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


def collectionlist(request):
    photos = Collection.objects.all()
    return render(request, 'photo/collection_list.html', {'collections': photos})


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})


def collection_detail(request, pk):
    collection = Collection.objects.get(id=pk)
    return render(request, 'photo/collection_detail.html', {'collection': collection})


def photo_detail(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})


def collection_create(request, pk):
    photo = Collection.objects.get(id=pk)
    return render(request, 'photo/collection_form.html', {'form': form})

    def post(self, request):
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_detail', pk=collection.pk)

        return render(request, 'photo/collection_form.html', {'form': form})


def photo_create(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_form.html', {'form': form})


def collection_edit(request, pk):
    collection = Collection.objects.get(pk=pk)
    if request.method == 'POST':
        form = CollectionForm(request.method == "POST", instance=colleciton)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_detail', pk=collection.pk)
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'collection_form.html', {'form': form})


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            collection = form.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_form.html', {'form': form})


def collection_delete(request, pk):
    Collection.objects.get(id=pk).delete()
    return redirect('collection_list')


def photo_delete(request, pk):
    Photo.objects.get(id=pk).delete()
    return redirect('photo_list')
