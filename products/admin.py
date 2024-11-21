from django.contrib import admin
from .models import Product, Category, Subcategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sell_price', 'buy_price', 'created_at', 'category')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'category')  # Zde stačí přímo 'category'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)