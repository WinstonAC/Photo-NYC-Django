from .models import Collection, Photo
from django.shortcuts import render, redirect
from.forms import CollecitonForm, PhotoForm


def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'photo/collection_list.html', {'collections': collection})


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})


def collection_detail(request, pk):
    collection = Collection.objects.get(id=pk)
    return render(request, 'photo/collection_detail.html', {'collection': artist})


def photo_detail(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})


def collection_create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_detail', pk=collection.pk)
    else:
        form = CollectionForm()
    return render(request, 'photo/colleciton_form.html', {'form': form})


def photo_create(request):
    if requested.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect('song_detail', pk=photo.pk)
        else:
            form = PhotoForm()
            return render(request, 'photo/photo_form.html', {'form': form})


def colleciton_edit(request, pk):
    collection = Collection.objects.get(pk=pk)
    if request.method == 'POST':
        form = CollectionForm(request.method == "POST", instance=colleciton)
        if form.is_valid():
            artist = form.save()
            return redirect('collection_detail', pk=collection.pk)
        else:
            form = CollecitonForm(instance=collection)
        return render(request, 'photo_form.html', {'form': form})


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


def colleciton_delte(request, pk):
    Collection.objects.get(id=pk).delete()
    return redirect('collection_list')


def photo_delete(request, pk):
    Photo.objects.get(id=pk).delete()
    return redirect('photo_list')
