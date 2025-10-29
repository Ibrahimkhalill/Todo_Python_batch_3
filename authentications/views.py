from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .form import RegistrationForm

from django.contrib.auth import authenticate, login, logout

def register(request):
    
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect("registration")
        
        messages.error(request, form.errors)
        return redirect("registration")
    else:
        
        form = RegistrationForm()
        context = {
            "form": form
        }
    
        return render(request, "registration.html", context)



def signin(request):
   if request.user.is_authenticated:
      return redirect('home') 
   else:
      if request.method == "POST":
         username = request.POST.get("username")
         password = request.POST.get("password")
         
         user = authenticate(request, username=username, password=password)
         
         if user is not None:
            login(request,user)
            return redirect("home")
         messages.error(request, "username or password is not valid")
         return redirect("signin")
         
      return render(request, "login.html")


def user_logout(request):
   logout(request)
   return redirect('signin')

              