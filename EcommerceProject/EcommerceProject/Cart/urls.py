from django.urls import path
from EcommerceProject.Cart.views import add_to_cart

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    # path('cart/', show_cart, name='show-cart'),

]