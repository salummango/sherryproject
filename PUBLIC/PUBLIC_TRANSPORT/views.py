from django.shortcuts import render
from .models import Passenger
from .forms import Passenger_forms
# Create your views here.
def homepage(request):
    return render(request=request,template_name='homepage.html')

def Passenger_view(request):
    if request.method=='POST':
        Passengerforms=Passenger_forms(request.POST)
        if Passengerforms.is_valid():
            Passengerforms.save()
    Passengerforms=Passenger_forms()
    return render(request=request,template_name='Passenger_view.html',context={'Passengerforms':Passengerforms})

def Passenger_list(request):
    passengers=Passenger.objects.all()
    return render(request,template_name="Passenger_list.html",context={'passengers':passengers})






