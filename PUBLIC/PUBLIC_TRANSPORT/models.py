from django.db import models

# Create your models here.
class Passenger(models.Model):
    Passenger_ID=models.AutoField(primary_key=True)
    Passenger_address= models.CharField(max_length=50)
    Passenger_phonenumber=models.IntegerField()
    def _str_(Self):
        return Self.Passenger