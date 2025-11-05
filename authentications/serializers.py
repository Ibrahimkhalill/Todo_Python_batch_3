from rest_framework import serializers

from .models import UserProfile
from django.contrib.auth.models import User




         
      
      
class ProfileSerializer(serializers.ModelSerializer):
  
   class Meta:
      model = UserProfile
      fields= ["id","phone_number","profile_picture"]
      

class RegisterSerializer(serializers.ModelSerializer):

   class Meta:
      model = User
      fields= ["id","username","first_name","last_name","password"]



class UserSerializer(serializers.ModelSerializer):
   user_profile = ProfileSerializer(required=False)
   class Meta:
      model = User
      fields= ["id","username","email","first_name","last_name","user_profile"]
      
        
  