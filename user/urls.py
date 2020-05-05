from django.urls import path, include
from .views import UserRegistration, CreateTokenView, search_user_view, Logout

urlpatterns = [
    path('logout/', Logout.as_view()),
    path('users/', search_user_view),
    path('registration', UserRegistration.as_view(), name='registration'),
    path('token', CreateTokenView.as_view(), name='token')
]