from .models import Category, Subcategory


def categories_and_subcategories(request):
    """
    Tento processor zpřístupní všechny kategorie a podkategorie
    filtrované podle aktuálně vybrané kategorie.
    """
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')

    if selected_category_id:
        subcategories = Subcategory.objects.filter(category_id=selected_category_id)
    else:
        subcategories = Subcategory.objects.none()  # Žádné podkategorie, pokud není vybraná kategorie

    return {
        'base_categories': categories,
        'base_subcategories': subcategories,
    }