from django.shortcuts import render,get_object_or_404,redirect
from account.models import User

# Create your views here.

user=0

class context:
	username=0

def adduser(request):
	username=request.POST['username']
	email=request.POST['email']
	password=request.POST['password']
	person=User(username=username,email=email,password=password)
	person.save()
	userlist={
		"username":username
		}
	return render(request,"userhome.html",{'userlist':userlist})

def user(request):
	uemail=request.POST['uemail']
	upassword=request.POST['upass']
	try:
		userlist=get_object_or_404(User,email=uemail)	
		global user 
		user = userlist.username
		context.username=user
	except:
		userlist=0	
	return render(request,"userhome.html",{'userlist':userlist})

def rentcar(request):
	return render(request,"rentcar.html",{"userstate":1,"user":user})

def userHome(request):
	return render(request,"userHomeAfterLogin.html",{"userstate":1,"user":user})