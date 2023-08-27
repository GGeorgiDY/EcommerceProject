from django.shortcuts import render
from django.views import View
from EcommerceProject.Accounts.models import Customer
from EcommerceProject.Cart.models import Cart
from EcommerceProject.EcommerceApp.models import Product


def home(request):
    # това дисплейва колко продукта имаме в количката, за да ги визуализира в навигацията
    totalitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))

    return render(request, "EcommerceApp/home.html", locals())


def about(request):
    totalitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
    return render(request, "EcommerceApp/about.html", locals())


def contact(request):
    totalitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
    return render(request, "EcommerceApp/contact.html")


# class CategoryView(View):
#     def get(self, request, val):
#         products = Product.objects.filter(category=val)
#         title = Product.objects.filter(category=val).values('title')
#         return render(request, "EcommerceApp/category.html", locals())


def category_view(request, val):
    totalitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))

    # вземи всички продукти със зададената категория
    products = Product.objects.filter(category=val)
    # тук пак взимаме всички продукти - правим го за да не зачезват всички изброени налични продукти в полето в ляво в страницата, като кликнем на един продукт.
    title = Product.objects.filter(category=val).values('title')
    return render(request, "EcommerceApp/category.html", locals())


# add more logic in category page to filter the products by their title
# class CategoryTitle(View):
#     def get(self, request, val):
#         products = Product.objects.filter(title=val)
#         title = Product.objects.filter(category=products[0].category).values('title')
#         return render(request, "EcommerceApp/category.html", locals())


def category_title(request, val):
    totalitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))

    products = Product.objects.filter(title=val)
    title = Product.objects.filter(category=products[0].category).values('title')
    return render(request, "EcommerceApp/category.html", locals())


# class ProductDetails(View):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         return render(request, "EcommerceApp/productdetails.html", locals())

def product_details(request, pk):
    totalitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))

    product = Product.objects.get(pk=pk)
    return render(request, "EcommerceApp/productdetails.html", locals())
