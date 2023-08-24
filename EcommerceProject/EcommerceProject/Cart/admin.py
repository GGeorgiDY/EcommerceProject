from django.contrib import admin
from EcommerceProject.Cart.models import Cart


@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
