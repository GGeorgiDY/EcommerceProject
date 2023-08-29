from django.urls import path
from EcommerceProject.Cart.views import add_to_cart, show_cart, minus_cart, remove_cart, plus_cart, checkout, \
    minus_wishlist, plus_wishlist, search, wishlist, search_predictions

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/', show_cart, name='show_cart'),
    path('checkout/', checkout.as_view(), name='checkout'),

    path('pluscart/', plus_cart, name='plus_cart'),
    path('minuscart/', minus_cart, name='minus_cart'),
    path('removecart/', remove_cart, name='remove_cart'),

    path('pluswishlist/', plus_wishlist, name='plus_wishlist'),
    path('minuswishlist/', minus_wishlist, name='minus_wishlist'),

    path('search/', search, name='search'),
    path('search-predictions/', search_predictions, name='search-predictions'),

    path('wishlist/', wishlist, name='wishlist'),
]