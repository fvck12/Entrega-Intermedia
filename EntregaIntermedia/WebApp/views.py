from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    
    return render(request, "index.html")

def about(request):
    
    return render(request, "about.html")

def post(request):
    
    return render(request, "post.html")

def contact(request):
    
    return render(request, "contact.html")