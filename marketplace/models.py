from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    UNIT_CHOICES = [
        ('KG', 'Kilogram'),
        ('GRAM', 'Gram'),
        ('LITER', 'Liter'),
        ('PIECE', 'Piece'),
        ('DOZEN', 'Dozen'),
        ('QUINTAL', 'Quintal'),
        ('SACK', 'Sack'), 
    ]
    CATEGORY_CHOICES = [
        ('VEGETABLES', 'Vegetables'),
        ('FRUITS', 'Fruits'),
        ('GRAINS', 'Grains'),
        ('SPICES', 'Spices'),
        ('DAIRY', ' Dairy'),
        ('MEAT', ' Meat'),
        ('LEGUMES', 'Legumes/Pulses'),
        ('OILSEEDS', 'Oilseeds'),
        ('OTHERS', 'Others'),

    ]
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,related_name='products')

    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=10 , choices=UNIT_CHOICES,default='KG') #measurement (KG, liter)
    quantity = models.DecimalField(decimal_places=2 , max_digits=10,validators=[MinValueValidator(0.01)])
    unit_price = models.DecimalField(decimal_places=2 , max_digits=10,validators=[MinValueValidator(0.01)]) #Price per unit
    category = models.CharField(max_length=50 , choices=CATEGORY_CHOICES ,default='VEGETABLES')
    district = models.CharField(max_length=50, blank=True,null=True, help_text="Location where product is available")
    is_available = models.BooleanField(default=True) 
    harvest_date = models.DateField(null=True, blank=True)
    image = models.ImageField(blank=True , null=True ,upload_to='product_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
