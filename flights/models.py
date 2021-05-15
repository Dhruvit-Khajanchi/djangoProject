from django.db import models

# Create your models here.
class airport(models.Model):
    city=models.CharField(max_length=10)
    code=models.CharField(max_length=50)

    def __str__(self):
        return f"({self.code}) {self.city}"

class flights(models.Model):
    depart=models.ForeignKey(airport, on_delete=models.CASCADE, related_name='departure')
    arrive=models.ForeignKey(airport, on_delete=models.CASCADE, related_name='arrival')
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.depart} - {self.arrive}"