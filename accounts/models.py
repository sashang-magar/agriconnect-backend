from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import NEPAL_DISTRICTS ,BUSINESS_TYPES
from django.conf import settings
from django.core.validators import MinValueValidator

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="farmerprofile")
    farm_name = models.CharField(max_length=255  , blank=True)
    farm_description = models.TextField(blank=True , null=True)
    is_verified = models.BooleanField(default=False)

    total_review = models.IntegerField( blank=True , null=True , default=0)
    total_rating_sum = models.IntegerField( default=0 , blank=True , null=True )
    average_rating = models.DecimalField(max_digits=3 , decimal_places=2 , default=0.00)

    def update_rating(self):
        """Update rating based on all reviews"""
        from marketplace.models import Review  # Import here to avoid circular import

        

class BuyerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="buyerprofile")
    address = models.TextField(blank=True)
    business_name= models.CharField(max_length=255 , blank=True)
    business_type = models.CharField(max_length=255 ,choices=BUSINESS_TYPES , blank=True)