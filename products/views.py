from django.shortcuts import render
from .models import Category, Subcategory, Product

def home(request):
    return render(request, 'home.html')

def products(request):
    categories = Category.objects.all()  # Načteme všechny kategorie
    category_id = request.GET.get('category')  # Získání ID vybrané kategorie z URL parametrů

    if category_id:
        subcategories = Subcategory.objects.filter(category_id=category_id)  # Filtrované podkategorie
        products = Product.objects.filter(subcategory__category_id=category_id)  # Produkty z vybrané kategorie
    else:
        subcategories = Subcategory.objects.none()  # Žádné podkategorie
        products = Product.objects.all()  # Všechny produkty

    return render(request, 'products.html', {
        'categories': categories,
        'subcategories': subcategories,
        'products': products
    })