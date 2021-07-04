from product.models import Product, Cart, Order
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from product.forms import OrderCheckOut

@csrf_exempt
def add_product_view(request):
    print('add view called', request.POST.get('id'))
    id = request.POST.get('id')
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0)+ 1
    request.session['cart'] =  cart
    return HttpResponse('Hi ')


@csrf_exempt
def delete_product_view(request):
    print('delete view  called', request.POST.get('id'))
    id = request.POST.get('id')
    cart = request.session['cart'] or {}
    cart[id] = cart.get(id, 1) - 1
    request.session['cart'] =  cart
    return HttpResponse('hi ')

def home_view(request):
    objs = Product.objects.all()
    request.session['cart'] = request.session.get('cart', {})
    return render(request, 'base.html', {'objs':objs})

def cart_show(request):
    '''
    '''
    return render(request, 'cart.html' )

def checkout(request):
    '''
    '''
    form = OrderCheckOut(request.POST or None)
    if form.is_valid():
        obj = form.save()
        
        for ele in request.session['cart']:
            print(ele, request.session['cart'][ele])
            cart = Cart.objects.create(cart=Product.objects.get(id=ele), 
                                        unit = request.session['cart'][ele],
                                        order= Order.objects.get(id=obj.id)
            )
            cart.save()
        
        del request.session['cart']
        return render(request, 'success.html')

    return render(request, 'checkout.html',{'form':form})

