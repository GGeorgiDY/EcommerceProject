from django.shortcuts import render, redirect, get_object_or_404
from EcommerceProject.Cart.models import Cart
from EcommerceProject.EcommerceApp.models import Product


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    # product = Product.objects.filter(id=product_id).get()
    product = get_object_or_404(Product, id=product_id)
    Cart(user=user, product=product).save()

    return redirect("/cart")


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'Cart/addtocart.html', locals())


def checkout(request):
    pass