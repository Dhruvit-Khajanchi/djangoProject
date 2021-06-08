from django.db import models

# Create your models here.

class employees(models.Model):
    name=models.CharField(max_length=50)
    phn=models.TextField()
    age=models.IntegerField(max_length=2)
    designation=models.TextField()