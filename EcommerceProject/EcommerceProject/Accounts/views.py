from django.contrib import messages
from django.shortcuts import render
from django.views import View
from EcommerceProject.Accounts.forms import CustomerRegistrationForm, CustomerProfileForm


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
        return render(request, 'Accounts/profile.html', locals())
