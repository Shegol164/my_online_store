from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView, TemplateView
)
from django.urls import reverse_lazy
from .models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

from django.views.generic import ListView
from .models import Product
from django.views.decorators.cache import cache_page
from .services import get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = 'moderation'
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'status']
    template_name = 'catalog/product_form.html'

    def test_func(self):
        product = self.get_object()
        return (product.owner == self.request.user or
                self.request.user.has_perm('catalog.can_change_product_status'))

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'

    def test_func(self):
        product = self.get_object()
        return (product.owner == self.request.user or
                self.request.user.has_perm('catalog.delete_product'))

    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

@cache_page(60 * 15)  # Кеширование на 15 минут
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def category_products(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'catalog/category_products.html', {'products': products})

def product_list(request):
    cache_key = 'all_products'
    products = cache.get(cache_key)
    if not products:
        products = Product.objects.all()
        cache.set(cache_key, products, 60 * 15)  # Кеширование на 15 минут
    return render(request, 'catalog/product_list.html', {'products': products})