from django.db import models
# Create your models here.
from datetime import date
class Blog(models.Model):
    author=models.CharField(max_length=20)
    topic=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    today=models.DateTimeField(default=date.today())
