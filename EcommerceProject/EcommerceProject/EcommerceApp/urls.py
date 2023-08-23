from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from EcommerceProject.EcommerceApp.views import home, CategoryView, ProductDetails, CategoryTitle, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('category-title/<val>', CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>', ProductDetails.as_view(), name='product-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
