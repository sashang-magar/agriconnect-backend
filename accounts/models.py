from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import NEPAL_DISTRICTS 

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


