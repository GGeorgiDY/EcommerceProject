from django.contrib import admin
from EcommerceProject.Accounts.models import Customer


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'zipcode']