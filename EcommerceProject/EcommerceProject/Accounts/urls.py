from django.contrib.auth import views as auth_view
from django.urls import path
from EcommerceProject.Accounts.forms import CustomerLoginForm, MyPasswordResetForm, MyPasswordChangeForm
from EcommerceProject.Accounts.views import CustomerRegistrationView, ProfileView, address, UpdateAddress

urlpatterns = [
    path("registration/", CustomerRegistrationView.as_view(), name="customerregistration"),

    # понеже го пишем така, не е необходимо да пишем вю
    path("login/", auth_view.LoginView.as_view(
        template_name='Accounts/customerlogin.html',
        authentication_form=CustomerLoginForm
    ), name="customerlogin"),

    path("password-reset/", auth_view.PasswordResetView.as_view(
        template_name='Accounts/password_reset.html',
        form_class=MyPasswordResetForm
    ), name="password_reset"),

    path("password-change/", auth_view.PasswordChangeView.as_view(
        template_name='Accounts/password_change.html',
        form_class=MyPasswordChangeForm,
        success_url='/account/password-change-done'
    ), name="password_change"),

    path("password-change-done/", auth_view.PasswordChangeDoneView.as_view(
        template_name='Accounts/password_change_done.html',
    ), name="password_change_done"),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('address/', address, name='address'),
    path('update-address/<int:pk>', UpdateAddress.as_view(), name='update-address'),
]