from django.contrib.auth import views as auth_view
from django.urls import path
from EcommerceProject.Accounts.forms import CustomerLoginForm, MyPasswordResetForm
from EcommerceProject.Accounts.views import CustomerRegistrationView, ProfileView

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

    path('profile/', ProfileView.as_view(), name='profile'),
    path('address/', ProfileView.as_view(), name='address'),
]