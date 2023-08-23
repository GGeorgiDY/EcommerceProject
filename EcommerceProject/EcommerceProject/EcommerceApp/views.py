from django.shortcuts import render
from django.views import View
from EcommerceProject.EcommerceApp.models import Product


def home(request):
    return render(request, "EcommerceApp/home.html")


def about(request):
    return render(request, "EcommerceApp/about.html")


def contact(request):
    return render(request, "EcommerceApp/contact.html")


class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "EcommerceApp/category.html", locals())


# add more logic in category page to filter the products by their title
class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        return render(request, "EcommerceApp/category.html", locals())


class ProductDetails(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "EcommerceApp/productdetails.html", locals())