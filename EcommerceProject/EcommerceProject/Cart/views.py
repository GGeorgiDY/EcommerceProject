from django.shortcuts import render, redirect
from django.urls import reverse

from EcommerceProject.Accounts.models import Customer
from EcommerceProject.Cart.models import Cart
from EcommerceProject.EcommerceApp.models import Product


def add_to_cart(request):
    my_user = request.user
    customer = Customer.objects.get(user=my_user)
    # print(user)
    #
    # product = Product.objects.get(id='1')
    # print(product)
    #
    # product_id = Cart.user.id
    # print(product_id)

    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=customer, product=product).save()

    # return redirect("/cart")
    return redirect(reverse('show-cart'))


def show_cart(request):
    user = Customer.objects.get(user=request.user)
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'Cart/addtocart.html', locals())


def checkout(request):
    pass