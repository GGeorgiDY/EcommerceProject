from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from EcommerceProject.Accounts.forms import CustomerRegistrationForm, CustomerProfileForm
from EcommerceProject.Accounts.models import Customer
from EcommerceProject.Cart.models import Cart, Wishlist


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


# @method_decorator(login_required, name='dispatch')
# class ProfileView(View):
#     def get(self, request):
#         totalitem = 0
#         wishitem = 0
#         user = Customer.objects.get(user=request.user)
#         if request.user.is_authenticated:
#             totalitem = len(Cart.objects.filter(user=user))
#             wishitem = len(Wishlist.objects.filter(user=request.user))
#
#         form = CustomerProfileForm()
#         return render(request, 'Accounts/profile.html', locals())
#
#     def post(self, request):
#         form = CustomerProfileForm(request.POST)
#         if form.is_valid():
#             user = request.user
#             name = form.cleaned_data['name']
#             lacality = form.cleaned_data['locality']
#             city = form.cleaned_data['city']
#             mobile = form.cleaned_data['mobile']
#             zipcode = form.cleaned_data['zipcode']
#
#             reg = Customer(user=user, name=name, locality=lacality, mobile=mobile, city=city, zipcode=zipcode)
#             reg.save()
#             messages.success(request, "Congratulations! Profile Save Successfully!")
#         else:
#             messages.warning(request, "Invalid Input Data!")
#
#         return render(request, 'Accounts/profile.html', locals())

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        user = Customer.objects.get(user=request.user)
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        form = CustomerProfileForm(instance=user)  # Pass the existing customer instance to the form
        return render(request, 'Accounts/profile.html', locals())

    def post(self, request):
        user = request.user
        user_customer = get_object_or_404(Customer, user=user)  # Get the existing customer instance

        form = CustomerProfileForm(request.POST, instance=user_customer)  # Update the instance with form data
        if form.is_valid():
            form.save()  # Save the form to update the existing customer instance
            messages.success(request, "Congratulations! Profile Saved Successfully!")
        else:
            messages.warning(request, "Invalid Input Data!")

        return render(request, 'Accounts/profile.html', locals())


@login_required
def address(request):
    totalitem = 0
    wishitem = 0
    user = Customer.objects.get(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    add = Customer.objects.filter(user=request.user)
    return render(request, "Accounts/address.html", locals())


@method_decorator(login_required, name='dispatch')
class UpdateAddress(View):
    def get(self, request, pk):
        totalitem = 0
        wishitem = 0
        user = Customer.objects.get(user=request.user)
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, "Accounts/updateAddress.html", locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile Update Successfully!")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')

