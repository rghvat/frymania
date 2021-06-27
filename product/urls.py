from django.urls import path

from product.views import (
    add_product_view,
    delete_product_view,
    home_view,
    cart_show,
    checkout,
)
urlpatterns = [
    path('add/',add_product_view),
    path('delete/',delete_product_view),
    path('', home_view),
    path('cart/', cart_show),
    path('checkout/',checkout),
]