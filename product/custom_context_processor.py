from .models import Product

def product_renderer(request):
    return {
       'all_product' : Product.objects.all(),
    }