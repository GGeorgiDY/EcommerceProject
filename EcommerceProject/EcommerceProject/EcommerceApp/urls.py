from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from EcommerceProject.EcommerceApp.views import home, about, contact, \
    category_view, category_title, product_details

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<slug:val>', category_view, name='category'),
    path('category-title/<val>', category_title, name='category-title'),
    path('product-detail/<int:pk>', product_details, name='product-detail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
