from django.urls import path
from . import views

urlpatterns = [
    path("rentcar/",views.rentCarHome,name="rentCar")
]