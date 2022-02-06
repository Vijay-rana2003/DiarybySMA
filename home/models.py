from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mydiary(models.Model):
    sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Description = models.TextField()
    Short_Description = models.CharField(max_length=300)
    Slug = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Time=models.DateTimeField(auto_now_add=True)

class contactuser(models.Model):
    Name = models.CharField(max_length=30) 
    Address=models.CharField(max_length=50)
    Description = models.TextField()
    Email=models.EmailField()
    Time=models.DateTimeField(auto_now_add=True)
