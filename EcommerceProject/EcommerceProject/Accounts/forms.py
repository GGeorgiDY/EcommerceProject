from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, \
    SetPasswordForm, PasswordResetForm


UserModel = get_user_model()


class CustomerRegistrationForm(auth_forms.UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': 'True',
                'class': 'form-control',
                'placeholder': 'Place you username here'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Place you email here'
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Place you passwort here'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Repeat your password here'
            }
        )
    )

    class Meta:
        model = UserModel
        fields = ("username", "password1", "password2", "email",)
        field_classes = {"username": auth_forms.UsernameField}


class CustomerLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus ':'True',
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete ':'current-password',
                'class':'form-control'
            }
        )
    )


class CustomerPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(
            attrs={
                'autofocus ':'True',
                'current-password':'form-control'
            }
        )
    )

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':'current-password',
                'current-password':'form-control'
            }
        )
    )

    new_password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':'current-password',
                'current-password':'form-control'
            }
        )
    )


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control'
            }
        )
    )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':'çurrent-password',
                'class':'form-control'
            }
        )
    )

    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':'çurrent-password',
                'class':'form-control'
            }
        )
    )


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'gender', 'locality', 'city', 'mobile', 'zipcode']
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            # 'gender': forms.TextInput(attrs={'class':'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }
