from django.shortcuts import render
from .models import flights
# Create your views here.

def home(request):
    return render(request, "flights/home.html", {
        "flight_list": flights.objects.all()
    })

def flight_info(request,flight_id):
    flight=flights.objects.get(pk=flight_id)
    return render(request, "flights/flight_details.html",{
        'flight_details':flight
    })