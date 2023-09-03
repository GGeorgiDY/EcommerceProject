from django.contrib.auth import views as auth_view
from django.urls import path, include
from EcommerceProject.Accounts.forms import MyPasswordResetForm, MySetPasswordForm
from EcommerceProject.Accounts.views import CustomerRegistrationView, CustomerLoginView, CustomerLogoutView, \
    PasswordChangeView, ProfileView, UpdateAddress, PasswordChangeDoneView, ChangeDetailsProfile, Address

urlpatterns = [
    path("registration/", CustomerRegistrationView.as_view(), name="customerregistration"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path('logout/', CustomerLogoutView.as_view(), name='logout'),

    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('profile/<int:pk>/', include([
        path('profile/', ProfileView.as_view(), name='profile'),
        path('change-profile-details/', ChangeDetailsProfile.as_view(), name='change_details_profile'),
        path('address/', Address.as_view(), name='address'),
        path('update-address/', UpdateAddress.as_view(), name='update-address'),
    ])),



    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='Accounts/password_reset.html',
        form_class=MyPasswordResetForm
    ), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='Accounts/password_reset_done.html',
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='Accounts/password_reset_confirm.html',
        form_class=MySetPasswordForm
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='Accounts/password_reset_complete.html',
    ), name='password_reset_complete'),

]

