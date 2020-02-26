from rest_framework import serializers

from .models import Photo, AdvancedUser


class PhotoSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='photo_detail', read_only=True, lookup_field='id')

    class Meta:
        model = Photo
        fields = (
            'id', 'name', 'url',
            'photo', 'owner_id', 'users'
        )

