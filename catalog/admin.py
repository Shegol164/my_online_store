from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status', 'owner')
    list_filter = ('status', 'owner')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'image')
        }),
        ('Статус', {
            'fields': ('status', 'owner')
        }),
    )