from django.shortcuts import render
from account.views import context
# Create your views here.
def about(request):
    return render(request,"before_login_about.html")

def userabout(request):
    user=context.username
    return render(request,"about.html",{"userstate":1,"user":user})