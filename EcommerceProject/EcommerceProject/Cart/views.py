from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from EcommerceProject.Cart.models import Cart, Wishlist
from EcommerceProject.EcommerceApp.models import Product
from django.contrib.auth import get_user_model

UserModel = get_user_model()

SHIPPING_TAX = 5.00


def add_to_cart(request):
    my_user = request.user
    # I get the product thanks to an input that I put in the html page and which is called "prod_id"
    # <input type="hidden" name="prod_id" value="{{ product.id }}">
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=my_user, product=product).save()
    return redirect(reverse('show_cart'))


@login_required
def show_cart(request):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    shipping = SHIPPING_TAX
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + shipping
    return render(request, 'Cart/addtocart.html', locals())


class Checkout(View):
    # decorator that checks if the user trying to access the page is logged in and if not redirects him to login page
    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        totalitem = 0
        wishitem = 0
        user = self.request.user
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=user))

        cart_items = Cart.objects.filter(user=user)
        famount = 0
        shipping = SHIPPING_TAX
        for p in cart_items:
            value = p.quantity*p.product.discounted_price
            famount = famount + value
        totalamount = famount + shipping
        return render(request, 'Cart/checkout.html', locals())


def plus_cart(request):
    user = request.user
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # Q is multiple filter condition
        # c is current cart object
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.quantity += 1
        c.save()

        cart = Cart.objects.filter(user=user)

        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + SHIPPING_TAX

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def minus_cart(request):
    user = request.user
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
        totalamount = amount + SHIPPING_TAX

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def remove_cart(request):
    user = request.user
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=user))
        c.delete()

        cart = Cart.objects.filter(user=user)

        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + SHIPPING_TAX

        data = {
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)

        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Wishlist Added Successfully',
        }

        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)

        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': 'Wishlist Remove Successfully',
        }

        return JsonResponse(data)


@login_required
def search(request):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    query = request.GET['search']
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'Cart/search.html', locals())


def search_predictions(request):
    query = request.GET.get('query', '')
    predictions = Product.objects.filter(title__icontains=query).values_list('title', 'id')

    return JsonResponse(list(predictions), safe=False)


def wishlist(request):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    wishlist = Wishlist.objects.filter(user=user)

    return render(request, 'Cart/wishlist.html', locals())