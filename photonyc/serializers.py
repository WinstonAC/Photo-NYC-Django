from rest_framework import serializers
from .models import Collection, Photo


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    # photos = serializers.HyperlinkedRelatedField(
    #     view_name='photo_detail',
    #     many=True,
    #     read_only=True
    # )
    # collection_url = serializers.ModelSerializer.serializer_url_field(
    #     view_name='collection_detail'
    # )

    class Meta:
        model = Collection
        fields = ('description',
                  'photo_url', 'name','id')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    # photos = serializers.HyperlinkedRelatedField(
    # view_name='photo_detail',
    # many=True,
    # read_only=True)

    collection = serializers.PrimaryKeyRelatedField(
         queryset=Collection.objects.all())


    class Meta:
        model = Photo
        fields = ('date', 'id',
                  'photo_url', 'title', 'location', 'collection')

class FormSerlizer()