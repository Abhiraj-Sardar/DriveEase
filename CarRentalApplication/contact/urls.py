from django.urls import path
from . import views

urlpatterns = [
    path("contact/",views.contact,name="contact"),
    path("user/contact/addcontact/",views.addcontact,name="addcontact"),
    path("contact/addContact/",views.addContact,name="addContact"),
    path("user/contact/",views.usercontact,name="usercontact")
]