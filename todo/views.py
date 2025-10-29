from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.
from .form import TodoForm 
from django.contrib import messages



def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('signin')


def about(request):
    return render(request, "about.html")



def get_all(request):
    print("request",request)
    
    todo_list = Todo.objects.all().order_by("-creat_at")
    context = {
        "data": todo_list,
        "html_title" : "Items page"
    }
    return render(request, "home.html", context)



def get_data_by_id(request, id):
    print("request",request)
    
    todo_list = Todo.objects.get(id=id)
    
    context = {
        "items": todo_list,
        "html_title" : "View Items page"
    }
    return render(request, "view_items.html", context)



def create(request):
    
    if request.method == "POST":
        print("request",request.FILES)
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Add Items successfully")
            return redirect("add-items")
        
        messages.error(request, "error adding items")
        return redirect("add-items")
    else:
        
        form = TodoForm()
        context = {
            "form": form
        }
    
        return render(request, "add_items.html", context)
    
    
    

def update(request, id):
    
    try:

     todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")
      
    if request.method =="POST":
        
        form = TodoForm(request.POST, instance=todo)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Items sucessfully updated")
            
            return redirect("update", id=todo.id)
        
        messages.error("error updating items")
        return redirect("update", id=todo.id)
   

    form = TodoForm(instance=todo)
    
    context = {
    "id": todo.id,
    "form": form
    }

    return render(request, "edit_items.html", context)
    

    

def delete(request, id):
    try:

     todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")

    todo.delete()
    messages.success(request, "Items deleted succesfully")
    return redirect("get-all")

