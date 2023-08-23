from django.contrib import messages
from django.shortcuts import render
from django.views import View
from EcommerceProject.Accounts.forms import CustomerRegistrationForm, CustomerProfileForm
from EcommerceProject.Accounts.models import Customer


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Accounts/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully!")
        else:
            messages.warning(request, "Invalid Input Data")

        return render(request, "Accounts/customerregistration.html", locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'Accounts/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            lacality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=lacality, mobile=mobile, city=city, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully!")
        else:
            messages.warning(request, "Invalid Input Data!")

        return render(request, 'Accounts/profile.html', locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "Accounts/address.html", locals())
