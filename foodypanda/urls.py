from django.urls import path
from .views import home,add_items
urlpatterns = [
    path("home/", home, name="Menu"),
    path("add_items/", add_items, name="add_items")
]