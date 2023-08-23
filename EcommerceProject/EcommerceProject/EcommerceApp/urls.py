from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from EcommerceProject.EcommerceApp.views import home, CategoryView, ProductDetails

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>', ProductDetails.as_view(), name='product-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
