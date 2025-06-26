from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'  # Пространство имён приложения

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
