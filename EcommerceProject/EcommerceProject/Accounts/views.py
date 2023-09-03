from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.urls import reverse_lazy

from EcommerceProject.Accounts.forms import CustomerRegistrationForm, CustomerProfileForm, CustomerPasswordChangeForm
from EcommerceProject.Cart.models import Cart, Wishlist
from EcommerceProject.Core.utils import OwnerRequired

# The name of the user model should be in only 2 places - in models.py and in settings.py. Everywhere else we should get
# it with the below way. The logic is that if the name of the user model is changed, it will return the correct one.
UserModel = get_user_model()
# self.request.user is the logged user. He represents the user who made the current request, if he is authenticated.
# If the user is not authenticated, self.request.user will be an instance of AnonymousUser.
# self.object is the selected user


class CustomerRegistrationView(views.CreateView):
    template_name = 'Accounts/customerregistration.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('customerlogin')


class CustomerLoginView(auth_views.LoginView):
    template_name = "Accounts/customerlogin.html"


class CustomerLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class PasswordChangeView(OwnerRequired, auth_views.PasswordChangeView):
    template_name = 'Accounts/password_change.html'
    model = UserModel
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy('profile')


class PasswordChangeDoneView(OwnerRequired, auth_views.PasswordChangeDoneView):
    template_name = 'Accounts/password_change_done.html'


class ProfileView(OwnerRequired, views.DetailView):
    template_name = 'Accounts/profile.html'
    model = UserModel
    form_class = CustomerProfileForm

    # decorator that checks if the user trying to access the page is logged in and if not redirects him to login page
    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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


class ChangeDetailsProfile(OwnerRequired, views.UpdateView):
    template_name = 'Accounts/change-details-profile.html'
    model = UserModel
    fields = ('username', 'first_name', 'last_name', 'email', 'gender')

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
class Address(OwnerRequired, views.DetailView):
    template_name = 'Accounts/address.html'
    model = UserModel

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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


class UpdateAddress(OwnerRequired, views.UpdateView):
    template_name = 'Accounts/updateAddress.html'
    model = UserModel
    fields = ('locality', 'mobile', 'city', 'zipcode')

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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


