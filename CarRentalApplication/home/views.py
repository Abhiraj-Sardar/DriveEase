from django.http import HttpResponse
from django.shortcuts import render
from account.models import User

# Create your views here.
def home(request):
    try:
        login=request.GET['user']
    except:
        login="not null"
    return render(request,'home.html',{"login":login})