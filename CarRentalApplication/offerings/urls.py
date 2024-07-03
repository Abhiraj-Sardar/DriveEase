from django.urls import path
from . import views

urlpatterns = [
    path("offers/",views.offers,name="offers"),
    path("user/offers/",views.useroffers,name="useroffers")
    
]