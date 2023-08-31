from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# from django.utils.decorators import method_decorator
from django.views import View
# from EcommerceProject.Accounts.forms import CustomerRegistrationForm, CustomerProfileForm
# from EcommerceProject.Accounts.models import Customer
# from EcommerceProject.Cart.models import Cart, Wishlist

from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views
from django.urls import reverse_lazy

from EcommerceProject.Accounts.forms import CustomerRegistrationForm, CustomerProfileForm, CustomerPasswordChangeForm
from EcommerceProject.Cart.models import Cart, Wishlist

UserModel = get_user_model()
# self.request.user е логнатия юзър
# self.object е селектирания юзър


class CustomerRegistrationView(views.CreateView):
    template_name = 'Accounts/customerregistration.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('customerlogin')


class CustomerLoginView(auth_views.LoginView):
    template_name = "Accounts/customerlogin.html"


class CustomerLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'Accounts/password_change.html'
    model = UserModel
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy('profile')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'Accounts/password_change_done.html'


class ProfileView(views.DetailView):
    template_name = 'Accounts/profile.html'
    model = UserModel
    form_class = CustomerProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        totalitem = 0
        wishitem = 0
        user = self.request.user
        if user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=user))

        context['is_owner'] = self.request.user == self.object
        context['totalitem'] = totalitem
        context['wishitem'] = wishitem

        return context


class ChangeDetailsProfile(views.UpdateView):
    template_name = 'Accounts/change-details-profile.html'
    model = UserModel
    fields = ('username', 'first_name', 'last_name', 'email', 'gender')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        totalitem = 0
        wishitem = 0
        user = self.request.user
        if user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=user))

        context['is_owner'] = self.request.user == self.object
        context['totalitem'] = totalitem
        context['wishitem'] = wishitem

        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={
            'pk': self.request.user.pk,
        })


# @login_required
class Address(views.DetailView):
    template_name = 'Accounts/address.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        totalitem = 0
        wishitem = 0
        user = self.request.user
        if user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=user))

        context['is_owner'] = self.request.user == self.object
        context['totalitem'] = totalitem
        context['wishitem'] = wishitem

        return context


# @method_decorator(login_required, name='dispatch')
class UpdateAddress(views.UpdateView):
    template_name = 'Accounts/updateAddress.html'
    model = UserModel
    fields = ('locality', 'mobile', 'city', 'zipcode')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        totalitem = 0
        wishitem = 0
        user = self.request.user
        if user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=user))
            wishitem = len(Wishlist.objects.filter(user=user))

        context['is_owner'] = self.request.user == self.object
        context['totalitem'] = totalitem
        context['wishitem'] = wishitem

        return context

    def get_success_url(self):
        return reverse_lazy('address', kwargs={
            'pk': self.request.user.pk,
        })


