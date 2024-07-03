from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    address=models.CharField(max_length=50)
    message=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)