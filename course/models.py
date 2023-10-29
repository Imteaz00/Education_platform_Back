from django.db import models
from authentication.models import Teacher

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100,blank=False, default = None)
    details = models.TextField(blank=False, default = None)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default = 0)
    # pic = models.ImageField(upload_to="images/")
    rating = models.DecimalField(max_digits=2, decimal_places=2, blank=False, default=0)
    techs = models.TextField(blank=False, default = None)
    content = models.FileField(blank = True, upload_to = "content")


    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE, default = None)

