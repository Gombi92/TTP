from django.contrib import admin
from .models import Product, Category, Subcategory
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sell_price', 'created_at', 'category', 'image_preview')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'category')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "Žádný obrázek"

    image_preview.short_description = "Náhled obrázku"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)