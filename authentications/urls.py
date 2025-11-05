from django.urls import path
from .views import register , profile, login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("registration/", register),
    path("profile/", profile),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
   
]