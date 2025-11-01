from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets

@api_view(["GET"])
def get_data(request):
   
   student = Student.objects.all()
   serializer = StudentSerializer(student, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)
   
   
class StudentList(APIView):
   """
   List all snippets, or create a new snippet.
   """

   def get(self, request, format=None):
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

   def post(self, request, format=None):
        print("data", request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
   def put(self, request,pk, format=None):
        print("data", request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListGenric(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudetRetUpDesGenric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class studentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    