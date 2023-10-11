from django.contrib import admin
from products.models import Product
# Register your models here.
@admin.register(Product)
class ProductaAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','image','is_new_arrival')