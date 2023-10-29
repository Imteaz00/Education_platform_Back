from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Student(User):
    name = models.CharField(max_length=100,blank=False, default = None)
    fullname = models.CharField(blank = False, max_length=100, default = None)
    it = models.TextField(blank=True)
    # pic = models.ImageField(upload_to="images/")

class Teacher(User):
    name = models.CharField(max_length=100,blank=False, default = None)
    fullname = models.CharField(blank = False, max_length=100, default = None)
    skills = models.TextField(blank=True)
    phone = models.CharField( max_length=10, blank=True)
    pic = models.ImageField(upload_to="images/", blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=2, blank=False, default=0)
    address = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, blank=True)
