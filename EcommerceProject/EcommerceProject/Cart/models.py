from django.contrib.auth.models import User
from django.db import models
from EcommerceProject.Accounts.models import Customer
from EcommerceProject.EcommerceApp.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
