from django.shortcuts import render
from .models import flights
# Create your views here.

def home(request):
    return render(request, "flights/home.html", {
        "flight_list": flights.objects.all()
    })