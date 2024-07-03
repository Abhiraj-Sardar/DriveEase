from django.shortcuts import render,redirect
from account.views import context
from contact.models import Contact
# Create your views here.
def contact(request):
    return render(request,"before_login_contact.html")

def usercontact(request):
    user=context.username
    return render(request,"contact.html",{"userstate":1,"user":user})

def addContact(request):
    name=request.POST['fname']
    email=request.POST['email']
    address=request.POST['address']
    message=request.POST['message']
    phone=request.POST['phone']
    person=Contact(name=name,email=email,address=address,message=message,phone=phone)
    person.save()
    user=context.username
    return redirect("/contact/")

def addcontact(request):
    name=request.POST['fname']
    email=request.POST['email']
    address=request.POST['address']
    message=request.POST['message']
    phone=request.POST['phone']
    person=Contact(name=name,email=email,address=address,message=message,phone=phone)
    person.save()
    user=context.username
    return redirect("/user/contact/")
    # return render(request,"contact.html",{"userstate":1,"user":user})

