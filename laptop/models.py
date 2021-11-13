from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Laptop(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=200,blank=True)
    COLOR_TYPE = (
        (1,'Grey'),
        (2,'Silver'),
        (3,'Black'),
        (4,'Red'),
        (4,'Blue'),
    )
    color = models.CharField(max_length=200,choices=COLOR_TYPE,blank=True)
    vin = models.IntegerField(blank=True,default=0)
    BRAND_TYPE = (
        (1,'Apple'),
        (2,'Asus'),
        (3,'Dell'),
        (4,'Lenovo'),
        (5,'Acer'),
    )
    brand = models.CharField(max_length=200,choices=BRAND_TYPE,blank=True)
    cpu = models.CharField(max_length=200,blank=True)
    ram = models.IntegerField(blank=True,default=0)
    memory = models.IntegerField(blank=True,default=0)
    DISPLAY_TYPE = (
        (1,'4096 x 2160'),
        (2,'2048 x 1080'),
        (3,'1920 x 1080'),
        (4,'1024 x 768'),
    )
    display = models.CharField(max_length=200,choices=DISPLAY_TYPE,blank=True)
    battery = models.IntegerField(blank=True,default=0)
    prod = models.CharField(max_length=200,blank=True)

