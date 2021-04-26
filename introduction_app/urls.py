from django.urls import path
from .views import home,about,search

urlpatterns = [
    path("home/", home, name="hello-home"),
    path("about/", about, name="about_page"),
    path("search/", search,name="search")
]