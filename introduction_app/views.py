from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h2>This is my First attempt: </h2>");

def about(request):
    return HttpResponse("<h1>About Page</h1>");

def search(request):
    return HttpResponse("<h5>Search files here</h5>");