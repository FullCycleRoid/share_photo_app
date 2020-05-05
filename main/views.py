from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from main.models import Photo
from main.serializers import PhotoSerializer


class PhotoListCreateViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user:
            return Response({"ERROR': 'Sorry you can't delete this object"},
                            status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)
