from django.shortcuts import render, redirect
from .models import house
from .forms import form_names


def index(request): 
    
    if request.method == "POST":
        form = form_names(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("info")
            
    return render(request, 'house/index.html', context={'form': form_names})    

def info(request):
    return render(request, 'house/main.html' ) 
    


# Create your views here.
