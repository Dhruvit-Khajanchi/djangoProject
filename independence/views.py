from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    date= datetime.utcnow()
    return render(request, "independence/home.html",
                  {'independence': date.month==8 and date.day==15
                   })