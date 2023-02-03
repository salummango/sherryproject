from django.urls import path
from . import views


app_name='PUBLIC_TRANSPORT'
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('passenger view',views.Passenger_view,name='Passenger view'),
    path('passenger list',views.Passenger_list,name='Passenger list')
]