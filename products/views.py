from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory, Product

def home(request):
    return render(request, 'home.html')

def products(request):
    categories = Category.objects.all()  # Načteme všechny kategorie
    category_id = request.GET.get('category')  # Získání ID vybrané kategorie z URL parametrů
    subcategory_id = request.GET.get('subcategory')

    if category_id and subcategory_id:
        # Filtrovat podle kategorie i podkategorie
        subcategories = Subcategory.objects.filter(category_id=category_id)
        products = Product.objects.filter(subcategory_id=subcategory_id)
    elif category_id:
        # Pokud je vybraná pouze kategorie, zobrazit všechny produkty z této kategorie
        subcategories = Subcategory.objects.filter(category_id=category_id)
        products = Product.objects.filter(subcategory__category_id=category_id)
    else:
        # Pokud není vybraná žádná kategorie ani podkategorie, zobrazit vše
        subcategories = Subcategory.objects.none()
        products = Product.objects.all()

    return render(request, 'products.html', {
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
        'selected_category_id': int(category_id) if category_id else None,  # Přidá aktuální ID kategorie
        'selected_subcategory_id': int(subcategory_id) if subcategory_id else None,  # Přidá aktuální ID podkategorie
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Načtení produktu nebo vrácení chyby 404

    return render(request, 'product_detail.html', {
        'product': product
    })