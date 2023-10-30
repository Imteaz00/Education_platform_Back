from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.    

class Userinfo(AbstractUser):
    fullname = models.CharField(max_length=100,blank=False, default = None)
    skills = models.TextField(blank=True, null= True)
    phone = models.CharField( max_length=10, blank=True, null= True)
    # pic = models.ImageField(upload_to="images/", blank=True, null= True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null= True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=False, default=0)
    address = models.CharField(max_length=200, blank=True, null= True)
    gender = models.CharField(max_length=10, blank=True, null= True)
    it = models.TextField(blank=True, null= True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return "UserInfo " + self.username
