from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    image=models.ImageField(upload_to="")
    price = models.DecimalField(max_digits=8,decimal_places=2)
    sale_price=models.DecimalField(max_digits=8,decimal_places=2)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)


class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)