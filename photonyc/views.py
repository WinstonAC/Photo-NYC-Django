from .models import Collection, Photo
from django.shortcuts import render, redirect
from .forms import CollectionForm, PhotoForm
from django.views import View
from django.views.generic import ListView, DetailView


class CollectionList(View):
    def get(self, request):
        collection = Collection.objects.all()
        return render(request, 'photo/collection_list.html', {'collections': collection})


class PhotoList(ListView):
    model = Photo
    context_object_name = 'photo'


def collection_detail(request, pk):
    collection = Collection.objects.get(id=pk)
    return render(request, 'photo/collection_detail.html', {'collection': collection})


class PhotoDetail(DetailView):
    queryset = Photo.objects.all()
    context_object_name = 'photo'


class CollectionCreate(View):
    form_class = CollectionForm
    template_name = 'photo/collection_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_detail', pk=collection.pk)
        return render(request, self.template_name, {'form': form})


class PhotoCreate(View):
    form_class = PhotoForm
    template_name = 'photo/photo_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect('photo_detail', pk=photo.pk)

        return render(request, self.template_name, {'form': form})


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
