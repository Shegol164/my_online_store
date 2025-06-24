from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import Product

# Класс для главной страницы
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

# Класс для страницы товара
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

# Класс для страницы контактов
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

# Альтернативный вариант FBV (если нужно)
'''
def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    return render(request, 'catalog/contacts.html')
'''