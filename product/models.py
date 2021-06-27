from django.db import models

# Create your models here.

class Product(models.Model):
    '''
    '''
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.FileField(upload_to='uploads/%Y/%m/%d/')
    price = models.SmallIntegerField(null=True, blank=True, default=10)

    def __str__(self):
        return self.name


class Order(models.Model):
    '''
    '''
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    address = models.TextField(null=True)
    on_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=12, null=True)

class Cart(models.Model):
    '''
    '''
    cart = models.ForeignKey(Product, related_name='products_in_cart', on_delete=models.SET_NULL, null=True)
    unit = models.SmallIntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    



