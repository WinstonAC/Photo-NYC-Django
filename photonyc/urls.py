from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectionList.as_view(), name='collection_list'),
    path('photos/', views.PhotoList.as_view(), name='photo_list'),
    path('collections/<int:pk>', views.collection_detail, name='collection_detail'),
    path('photo/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'),
    path('collection/new', views.CollectionCreate.as_view(),
         name='collection_create'),
    path('photos/new', views.PhotoCreate.as_view(), name='photo_create'),
    path('collections/<int:pk>/edit',
         views.collection_edit, name='collection_edit'),
    path('photos/<int:pk>/edit', views.photo_edit, name='photo_edit'),
    path('collectons/<int:pk>/delete',
         views.collection_delete, name='collection_delete'),
    path('photos/<int:pk>/delete', views.photo_delete, name='photo_delete'),

]
