from django.urls import path
from EcommerceProject.EcommerceApp.views import home

urlpatterns = (
    path('', home, name='home'),
)