from django.urls import path
from . import views

urlpatterns = [
    path('', views.collectionlist, name='collectiton_list'),
    path('photos/', views.photo_list, name='photo_list'),
    path('collections/<int:pk>', views.collection_detail, name='collection_detail'),
    path('photos/<int:pk>', views.photo_detail, name='photo_detail'),
    path('collections/new', views.collection_create, name='collection_create'),
    path('photos/new', views.photo_create, name='photo_create'),
    path('collections/<int:pk>/edit',
         views.collection_edit, name='collection_edit'),
    path('photos/<int:pk>/edit', views.photo_edit, name='photo_edit'),
    path('collectons/<int:pk>/delete', views.collection_delete, name='collection_delete'),
    path('photos/<int:pk>/delete', views.photo_delete, name='photo_delete'),

]
