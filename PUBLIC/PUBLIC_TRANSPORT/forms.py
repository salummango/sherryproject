from django import forms
from .models import Passenger
 

class Passenger_forms(forms.ModelForm):
    class Meta:
        model=Passenger
        fields=('Passenger_address','Passenger_phonenumber')