from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem, Product
from django.contrib import messages
from django.contrib.messages import get_messages


@login_required
def user_profile(request, user_id):
    # Kontrola, zda aktuální uživatel odpovídá ID v URL
    if request.user.id != user_id:
        raise Http404("Nemáte oprávnění zobrazit tento profil.")
    return render(request, 'user_profile.html', {'user': request.user})
    # Získání aktuálního košíku
    cart = get_or_create_cart(request)

    # Načtení položek v košíku
    cart_items = CartItem.objects.filter(cart=cart)

    # Spočítání celkové ceny
    total_price = sum(item.product.sell_price for item in cart_items)

    return render(request, 'user_profile.html', {
        'user': request.user,
        'cart_items': cart_items,
        'total_price': total_price,
    })

def get_or_create_cart(request):
    """
    Pomocná funkce pro získání nebo vytvoření košíku.
    Rozlišuje přihlášeného a nepřihlášeného uživatele.
    """
    if request.user.is_authenticated:
        # Pokud je uživatel přihlášen, použijeme jeho uživatelské ID
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        # Pokud není přihlášen, použijeme session pro uložení košíku
        cart_id = request.session.get('cart_id')
        if not cart_id:
            # Pokud session neobsahuje košík, vytvoříme nový
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
        else:
            # Pokud košík existuje v session, načteme ho
            cart = get_object_or_404(Cart, id=cart_id)

    return cart


def add_to_cart(request, product_id):

    if request.method == "POST":
        # Načtení produktu nebo vyvolání chyby 404, pokud neexistuje
        product = get_object_or_404(Product, id=product_id)

        # Získání nebo vytvoření košíku pomocí funkce get_or_create_cart
        cart = get_or_create_cart(request)

        # Přidání položky do košíku
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            messages.warning(request, f"Produkt '{product.name}' je již v košíku.")
        else:
            messages.success(request, f"Produkt '{product.name}' byl úspěšně přidán do košíku.")

        # Získání zpráv z Django messages a vrácení v JSON odpovědi
        storage = get_messages(request)
        message_list = [{'level': message.level, 'message': message.message, 'tags': message.tags} for message in
                        storage]

        return JsonResponse({'messages': message_list}, status=200)

    return JsonResponse({'error': 'Neplatný požadavek.'}, status=400)

def cart_view(request):
    # Získání aktuálního košíku
    cart = get_or_create_cart(request)

    # Načtení položek v košíku
    cart_items = CartItem.objects.filter(cart=cart)

    # Spočítání celkové ceny
    total_price = sum(item.product.sell_price for item in cart_items)

    # Předání dat šabloně
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })