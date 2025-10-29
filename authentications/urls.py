from django.urls import path
from .views import register , signin , user_logout

urlpatterns = [
    path("registration/", register , name="registration"),
    path("login/", signin, name="signin"),
    path("logout/", user_logout, name="logout"),
]