from django import forms

class EmployeesRegisterForm(forms.Form):
    name= forms.CharField(max_length=30, min_length=10)
    phn=forms.CharField(max_length=12, min_length=12)
    age=forms.IntegerField(min_value=2, max_value=2)
    designation=forms.CharField(max_length=75)