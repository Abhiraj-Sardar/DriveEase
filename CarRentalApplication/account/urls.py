from django.urls import path
from . import views

urlpatterns = [
    path("AddUser/",views.adduser,name="addUser"),
    path("user/",views.user,name="user"),
    path("user/rentcar/",views.rentcar,name="rentcar"),
    path("userHome/",views.userHome,name="userHome")
]