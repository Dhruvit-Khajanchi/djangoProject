from django.shortcuts import render
from django import forms
# Create your views here.
menu=[
    "Tomato Soup",
    "Hot & Sour",
    "Manchow",
    "Sweet Corn",
    "Broccoli Almond"
]

class NewItemForm(forms.Form):
    items=forms.CharField(max_length=25)
    qty=forms.IntegerField(max_value=10, min_value=1)
    status=forms.ChoiceField(choices=[('active', 'active'),
                                      ('deactive', 'deactive')])

def home(request):
    return render(request, "foodypanda/menu_list.html",{
        "menu":menu
    })

def add_items(request):
    form=NewItemForm()
    return render(request, "foodypanda/add_items.html",{
        'form':form
    })