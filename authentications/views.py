from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from .models import UserProfile
from .serializers import UserSerializer, ProfileSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response 
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
     
@api_view(["POST"])
def register(request):
   
   serializer = RegisterSerializer(data=request.data)
   
   if serializer.is_valid():
      user = serializer.save()  
      user.set_password(serializer.validated_data["password"])  
      user.save()
         
      user_serailzer = UserSerializer(user)
      refresh = RefreshToken.for_user(user)
      
      context = {
         "message" : "User successfully registered",
         "access_token": str(refresh.access_token),
         "refresh_token": str(refresh),
         "user": user_serailzer.data
      }
      
      return Response(context, status=201)
   
   return Response(serializer.errors, status=400)

@api_view(["POST"])      
def login(request):
   
   username = request.data.get("username")
   password = request.data.get("password")
   
   user = authenticate(username=username, password=password)
   print(user)
   if user:
      
      refresh = RefreshToken.for_user(user)
      user_serailzer = UserSerializer(user)
      context = {
         "access_token": str(refresh.access_token),
         "refresh_token": str(refresh),
         "user": user_serailzer.data
      }
      
      return Response(context, status=200)
   
   return Response({"error":"Username or Password is invalid"}, status=401)
   
   
      
      
@api_view(["GET"])
@permission_classes([IsAuthenticated])   
def profile(request):
   
   user = request.user

   profile_serializer = UserSerializer(user)
   
   return Response(profile_serializer.data, status=200)
   
    
   




              