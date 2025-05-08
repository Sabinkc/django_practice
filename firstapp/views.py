from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def sabin(request):
    return HttpResponse("Hello Sabin")

def greet(request, name):
    return HttpResponse(f"Hello {name}")

def renderhtml(request):
    return render(request,"firstapp/index.html", {
        "name":"sabin",
    })