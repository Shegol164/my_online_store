from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
