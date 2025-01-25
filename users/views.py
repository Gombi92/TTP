from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem, Product
from django.contrib import messages
from django.contrib.messages import get_messages
from ecommerce_project import views
from django.contrib.auth import logout


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
    cart = get_or_create_cart(request)  # Funkce pro získání aktuálního košíku
    cart_items = cart.items.all()  # Načtení všech položek v košíku
    total_price = sum(item.total_price for item in cart_items)  # Výpočet celkové ceny

    context = {
        'cart_items': cart_items,
        'total_price': total_price,  # Předání celkové ceny do šablony
    }
    print(f"Cart Items: {cart_items}")
    print(f"Total Price: {total_price}")

    return render(request, template_name='cart.html', context=context)


def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart = get_or_create_cart(request)
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

        if cart_item:
            cart_item.delete()
            messages.success(request, f"Produkt byl úspěšně odebrán z košíku.")
        else:
            messages.error(request, f"Produkt nebyl nalezen v košíku.")
        return redirect('cart')
    return JsonResponse({'error': 'Neplatný požadavek.'}, status=400)


def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Úspěšně jste se odhlásili!')
    return redirect('home')

def cart(request):
    # Můžete přidat logiku pro zobrazení košíku, pokud máte session nebo databázi
    return render(request, 'cart.html')