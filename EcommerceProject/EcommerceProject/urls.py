from django.contrib import admin
from django.urls import path, include

from EcommerceProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("EcommerceProject.EcommerceApp.urls")),
    path('account/', include("EcommerceProject.Accounts.urls")),
    path('cart/', include("EcommerceProject.Cart.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
