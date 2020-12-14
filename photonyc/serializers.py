from rest_framework import serializers
from .models import Collection, Photo


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.HyperlinkedRelatedField(
        view_name='photo_detail',
        many=True,
        read_only=True
    )
    collection_url = serializers.ModelSerializer.serializer_url_field(
        view_name='collection_detail'
    )

    class Meta:
        model = Collection
        fields = ('description', 'collection_url',
                  'photo_url', 'name', 'photos',)


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.HyperlinkedRelatedField(
        view_name='photo_detail',
        many=True,
        read_only=True
    )
    photo_url = serializers.ModelSerializer.serializer_url_field(
        view_name='collection_detail'
    )

    class Meta:
        model = Collection
        fields = ('date', 'collection_url',
                  'photo_url', 'title', 'photo', 'location',)
