from django.urls import path
from .views import home,about,greetings,greeting2

urlpatterns = [
    path("home/", home, name="hello-home"),
    path("about/", about, name="about_page"),
    path("greetings/<str:name>", greetings,name="greeting"),
    path("greetings/", greeting2,name="greetings2")
]