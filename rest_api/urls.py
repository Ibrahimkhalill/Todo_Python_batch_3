from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    get_data,
    StudentList,
    studentViewSet,
    StudentListGenric,
    StudetRetUpDesGenric
)

router = DefaultRouter()
router.register(r'students', studentViewSet, basename='student')

urlpatterns = [
    path("get/student-list/", StudentListGenric.as_view()),
    path("get/student-list/<int:pk>/", StudetRetUpDesGenric.as_view()),
    path('', include(router.urls)),  
]

