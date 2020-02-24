from django.urls import path
from .views import SignUpView, LoginView, LogoutView, UserSearchView, UserShareView

urlpatterns = [
    path('signup/', SignUpView),
    path('login/', LoginView),
    path('logout/', LogoutView),
    path('user', UserSearchView),
    path('user/<int:id>/share', UserShareView),
]