from rest_framework import serializers
import uuid
from .models import Photo, AdvancedUser


class PhotoSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(initial=uuid.uuid4)
    url = serializers.HyperlinkedIdentityField(view_name='photo-detail', lookup_field='id', read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'name', 'photo', 'url', 'owner', 'users')

