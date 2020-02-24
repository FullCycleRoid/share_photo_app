from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer


class PhotoDetailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self, id):
        obj = get_object_or_404(Photo, id=id)
        if self.request.user == obj.owner_id:
            return obj
        return

    def get(self, request, id, format=None):
        photo = self.get_object(id)
        self.serializer = PhotoSerializer(photo, context={'request': request})
        serializer = self.serializer
        return Response(serializer.data)

    def put(self, request, id, format=None):
        photo = self.get_object(id)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id, format=None):
        photo = self.get_object(id)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoView(ListAPIView, CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        qs = Photo.objects.filter(owner_id=user)
        return qs
