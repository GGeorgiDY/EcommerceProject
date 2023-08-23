from django.shortcuts import render
from django.views import View
from EcommerceProject.EcommerceApp.models import Product


def home(request):
    return render(request, "EcommerceApp/home.html")


class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        return render(request, "EcommerceApp/category.html", locals())
