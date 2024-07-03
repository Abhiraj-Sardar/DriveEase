from django.urls import path
from . import views

urlpatterns = [
    path("blog/",views.blogHome,name="blogHome"),
     path("user/blog/addpost/",views.addpost,name="addpost"),
    path("user/blog/",views.userblog,name="userblog")
]