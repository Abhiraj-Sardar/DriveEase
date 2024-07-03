from django.shortcuts import render
from account.views import context
# Create your views here.

def offers(request):
    return render(request,"before_login_offerings.html")

def useroffers(request):
    user=context.username
    return render(request,"offerings.html",{"userstate":1,"user":user})
