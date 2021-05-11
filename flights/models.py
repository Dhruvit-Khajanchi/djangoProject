from django.db import models

# Create your models here.

class flights(models.Model):
    depart=models.CharField(max_length=50)
    arrive=models.CharField(max_length=50)
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.depart} - {self.arrive}"