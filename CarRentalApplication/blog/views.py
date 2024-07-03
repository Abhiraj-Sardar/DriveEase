from django.shortcuts import redirect, render
from account.views import context
from datetime import date
from blog.models import Blog
# Create your views here.
def blogHome(request):
    return render(request,"before_login_blog.html")

def userblog(request):
    user=context.username
    posts=Blog.objects.all()
    posts_list=posts.values()
    
    return render(request,"blogpost.html",{"userstate":1,"user":user,"posts":posts_list})

def addpost(request):
    author=request.POST['author']
    topic=request.POST['topic']
    desc=request.POST['desc-topic']
    today=date.today()
    person=Blog(author=author,topic=topic,desc=desc,today=today)
    person.save()
    return redirect("/user/blog/")