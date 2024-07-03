from django.shortcuts import render

# Create your views here.
def rentCarHome(request):
    return render(request,"rentcar.html")