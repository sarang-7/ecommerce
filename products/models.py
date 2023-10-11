from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="products")
    is_new_arrival = models.BooleanField(default=False)