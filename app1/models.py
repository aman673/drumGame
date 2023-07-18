from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
]
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    country = models.CharField(max_length=20)


class Merchant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    country  =models.CharField(max_length=20)
    licence_no = models.CharField(max_length=20)
    GST_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    price  =models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    seller  =models.ForeignKey(Merchant,on_delete=models.CASCADE)
    cover_image = models.OneToOneField('Product_images' ,on_delete=models.CASCADE,related_name='item')
        # related_name reverse access allowed karta h
    def __str__(self) -> str:
        return self.name
        
 
class Product_images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null =True,blank = True)
    image = models.ImageField(upload_to='products/') 
# ye images ko media ke ander products folder me save kar dega

