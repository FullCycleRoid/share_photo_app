from django.conf.urls import url
from django.urls import path
from .views import PhotoView, PhotoDetailView

urlpatterns = [
    path('photo', PhotoView.as_view(), name='photos'),
    path(r'photo/<uuid:id>', PhotoDetailView.as_view(), name='photo_detail'),
]