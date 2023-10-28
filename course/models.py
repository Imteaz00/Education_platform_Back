from django.db import models

# Create your models here.


class course(models.Model):
    name = models.CharField(max_length=100,blank=False)
    details = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    # pic = models.ImageField(upload_to="images/")
    rating = models.DecimalField(max_digits=2, decimal_places=2, blank=False, default=0)


