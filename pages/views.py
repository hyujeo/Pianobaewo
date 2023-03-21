from django.shortcuts import render
from time import sleep

context = {"root": "http://127.0.0.1:8000/"}
# http://hyunhoj84.pythonanywhere.com/

# Create your views here.
def home(request):
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", context)

def resources(request):
    return render(request, "resources.html", context)

def credit(request):
    return render(request, "credit.html", context)

def basic(request):
    return render(request, "basic-index.html", context)

def cover(request):
    return render(request, "cover-index.html", context)

def comp(request): 
    return render(request, "comp-index.html", context)