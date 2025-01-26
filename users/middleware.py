from .models import Cart

from users.models import Cart
from django.db import IntegrityError

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                # Odstraňte duplicitní košíky, pokud existují
                carts = Cart.objects.filter(user=request.user)
                if carts.count() > 1:
                    carts.exclude(id=carts.first().id).delete()

                # Získejte nebo vytvořte jedinečný košík
                cart, created = Cart.objects.get_or_create(user=request.user)

                # Přesuňte anonymní košík do přihlášeného uživatele
                session_cart_id = request.session.pop('cart_id', None)
                if session_cart_id:
                    session_cart = Cart.objects.filter(id=session_cart_id).first()
                    if session_cart and session_cart != cart:
                        session_cart.user = request.user
                        session_cart.save()
                        cart = session_cart

                request.cart = cart
            except IntegrityError:
                # Pokud dojde k chybě integrity, načtěte existující košík
                request.cart = Cart.objects.filter(user=request.user).first()
        else:
            # Nepřihlášený uživatel: používejte session cart
            cart_id = request.session.get('cart_id')
            if not cart_id:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
            else:
                cart = Cart.objects.filter(id=cart_id).first()
                if not cart:
                    cart = Cart.objects.create()
                    request.session['cart_id'] = cart.id

            request.cart = cart

        response = self.get_response(request)
        return response