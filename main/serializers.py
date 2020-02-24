from rest_framework import serializers

from .models import Photo


# class PhotoSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='photo_detail', read_only=True)
#
#     class Meta:
#         model = Photo
#         fields = ('name', 'url', 'photo', 'owner_id', 'users')
#         # extra_kwargs = {
#         #     'url': {'view_name': 'photo-detail', 'lookup_field': 'id'},
#         # }


class PhotoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='photo_detail', read_only=True, lookup_field='id')

    class Meta:
        model = Photo
        fields = ('id', 'name', 'url',
                  'photo', 'owner_id', 'users')
