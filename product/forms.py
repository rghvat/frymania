from product.models import Order
from django import forms
from product.models import Order

class OrderCheckOut(forms.ModelForm):
    '''
    '''
    
    class Meta:
        model = Order
        fields = ['email', 'mobile', 'address']
