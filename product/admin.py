from django.contrib import admin

# Register your models here.
from product.models import Product, Cart, Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
