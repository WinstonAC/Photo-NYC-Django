from rest_framework import serializers
from .models import Collection

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.HyperlinkedRelatedField(
        view_name='photo_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Collection
        fields = ('description', 'photo_url', 'name',)