# from typing_extensions import Required
from django import template
from ..models import Product
register = template.Library()

@register.simple_tag(takes_context=True)
def mydict(context, key):
    request = context['request']
    print(request.session['cart'])
    return request.session['cart'].get(str(key), 0)

@register.simple_tag(takes_context=True)
def no_cart_items(context):
    request = context['request']
    return sum(value for ele, value in request.session['cart'].items())


@register.simple_tag(takes_context=True)
def get_product_name(context, key):
    for obj in Product.objects.all():
        if obj.id == int(key):
            return obj.name
