from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import NEPAL_DISTRICTS ,BUSINESS_TYPES
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('FARMER' ,'Farmer'),
        ('BUYER' ,'Buyer'),
        ('ADMIN' ,'Admin')
    ]
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True)
    district = models.CharField(max_length=50 , blank=True , choices= NEPAL_DISTRICTS)
    role = models.CharField(max_length=20 ,blank=False , choices=ROLE_CHOICES)


class FarmerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=255  , blank=True)
    farm_description = models.TextField(blank=True , null=True)
    is_verified = models.BooleanField(default=False)

class BuyerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    business_name= models.CharField(max_length=255 , blank=True)
    business_type = models.CharField(max_length=255 ,choices=BUSINESS_TYPES , blank=True)