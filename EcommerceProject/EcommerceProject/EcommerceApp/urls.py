from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from EcommerceProject.EcommerceApp.views import home, CategoryView

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
