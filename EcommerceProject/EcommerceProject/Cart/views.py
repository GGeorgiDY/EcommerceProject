from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from EcommerceProject.Accounts.models import Customer
from EcommerceProject.Cart.models import Cart
from EcommerceProject.EcommerceApp.models import Product


def add_to_cart(request):
    my_user = request.user
    customer = Customer.objects.get(user=my_user)

    # взимам продукта благодарение на един инпут, който съм сложил в html страницата и който се казва prod_id
    # <input type="hidden" name="prod_id" value="{{ product.id }}">
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


class checkout(View):
    def get(self, request):
        user = Customer.objects.get(user=request.user)
        add = Customer.objects.filter(user=request.user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity*p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40
        return render(request, 'Cart/checkout.html', locals())


def plus_cart(request):
    user = Customer.objects.get(user=request.user)
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # Q е multiple filter condition
        # c е current cart object
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity += 1
        c.save()

        # тук отново трябва да вземе юзъра и текущата карта
        cart = Cart.objects.filter(user=user)

        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def minus_cart(request):
    user = Customer.objects.get(user=request.user)
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity -= 1
        c.save()

        cart = Cart.objects.filter(user=user)

        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def remove_cart(request):
    user = Customer.objects.get(user=request.user)
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.delete()

        cart = Cart.objects.filter(user=user)

        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)
