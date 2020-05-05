from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoListCreateViewSet

router = DefaultRouter()
router.register('photo', PhotoListCreateViewSet)
urlpatterns = [
    path('', include(router.urls))
]