from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from EcommerceProject.Accounts.models import AppUser
from EcommerceProject.Cart.models import Cart, Wishlist
from EcommerceProject.EcommerceApp.models import Product
from django.contrib.auth import get_user_model

UserModel = get_user_model()

SHIPPING_TAX = 5.00

# @login_required
def add_to_cart(request):
    my_user = request.user
    # customer = Cart.user.objects.get(user=my_user)
    # customer = Cart.user

    # взимам продукта благодарение на един инпут, който съм сложил в html страницата и който се казва prod_id
    # <input type="hidden" name="prod_id" value="{{ product.id }}">
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=my_user, product=product).save()

    # return redirect("/cart")
    return redirect(reverse('show_cart'))


# @login_required
def show_cart(request):
    totalitem = 0
    wishitem = 0
    # user = Customer.objects.get(user=request.user)
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    # user = Customer.objects.get(user=request.user)
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    shipping = SHIPPING_TAX
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + shipping
    return render(request, 'Cart/addtocart.html', locals())


# когато имаме класове се използва това вместо @login_required
# @method_decorator(login_required, name='dispatch')
class checkout(View):
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


@login_required
def plus_cart(request):
    user = request.user
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
        totalamount = amount + SHIPPING_TAX

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


@login_required
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


@login_required
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


@login_required
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


@login_required
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
    # user = Customer.objects.get(user=request.user)
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    query = request.GET['search']
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'Cart/search.html', locals())


def search_predictions(request):
    query = request.GET.get('query', '')
    # predictions = Product.objects.filter(title__icontains=query).values_list('title', flat=True)
    predictions = Product.objects.filter(title__icontains=query).values_list('title', 'id')

    return JsonResponse(list(predictions), safe=False)


@login_required
def wishlist(request):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    wishlist = Wishlist.objects.filter(user=user)

    return render(request, 'Cart/wishlist.html', locals())