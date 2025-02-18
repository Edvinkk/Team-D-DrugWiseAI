from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")

def index(request):
    return render(request, "myapp/index.html")

def chat(request):
    return render(request, "myapp/chat.html")
