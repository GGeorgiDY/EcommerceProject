from django.contrib import admin
from EcommerceProject.Cart.models import Cart, Wishlist


@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(Wishlist)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']
