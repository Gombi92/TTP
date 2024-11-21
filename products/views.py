from django.shortcuts import render
from .models import Category, Subcategory, Product

def home(request):
    return render(request, 'home.html')

def product_list(request, category_id=None):
    categories = Category.objects.all()  # Načítá všechny kategorie
    subcategories = Subcategory.objects.filter(category_id=category_id) if category_id else None
    products = Product.objects.filter(subcategory__category_id=category_id) if category_id else None
    return render(request, 'products.html', {
        'categories': categories,
        'subcategories': subcategories,
        'products': products
    })