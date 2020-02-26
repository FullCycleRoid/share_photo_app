from django.urls import path, include
from .views import UserRegistration

urlpatterns = [
    path('registration', UserRegistration.as_view(), name='registration'),
]