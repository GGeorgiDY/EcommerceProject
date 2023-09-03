from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from EcommerceProject.Cart.models import Cart, Wishlist
from EcommerceProject.EcommerceApp.models import Product
from django.contrib.auth import get_user_model


UserModel = get_user_model()


def home(request):
    # this displays how many products we have in the cart to visualize them in the navigation
    totalitem = 0
    # this displays how many products we have liked
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    return render(request, "EcommerceApp/home.html", locals())


# decorator that checks if the user trying to access the page is logged in and if not redirects him to login page
@login_required
def about(request):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    return render(request, "EcommerceApp/about.html", locals())


@login_required
def contact(request):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    return render(request, "EcommerceApp/contact.html", locals())


class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "EcommerceApp/category.html", locals())


def category_view(request, val):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    # get all products with the specified category
    products = Product.objects.filter(category=val)
    # here again we take all the products - we do it so that all listed available products do not disappear in the
    # field on the left of the page by clicking on one product.
    title = Product.objects.filter(category=val).values('title')
    return render(request, "EcommerceApp/category.html", locals())


# add more logic in category page to filter the products by their title
class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        return render(request, "EcommerceApp/category.html", locals())


def category_title(request, val):
    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    products = Product.objects.filter(title=val)
    title = Product.objects.filter(category=products[0].category).values('title')
    return render(request, "EcommerceApp/category.html", locals())


class ProductDetails(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "EcommerceApp/productdetails.html", locals())


def product_details(request, pk):
    product = Product.objects.get(pk=pk)

    totalitem = 0
    wishitem = 0
    user = request.user
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))

    return render(request, "EcommerceApp/productdetails.html", locals())

