from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("EcommerceProject.EcommerceApp.urls")),
    path('account/', include("EcommerceProject.Accounts.urls")),
]
