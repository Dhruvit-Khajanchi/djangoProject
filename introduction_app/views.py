from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h2>This is my First attempt: </h2>");
    return render(request, "introduction_app/home.html",
                  { 'title':'Home'

                  })

def about(request):
    # return HttpResponse("<h1>About Page</h1>");
    return render(request, "introduction_app/about.html",
                  { 'title': 'About'

                  })

def greetings(request,name):
    # return HttpResponse("<h5>Hello Dhruvit</h5>");
    return render(request, "introduction_app/greetings.html",
                  {'username':name,
                   'title':'Greetings'
    })

def greeting2(request):
    return render(request,"introduction_app/greeting2.html",
                  {'title':'Greeting'

                  })