from .models import Cart

from users.models import Cart


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Přihlášený uživatel: získejte nebo vytvořte Cart
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Pokud má uživatel anonymní košík, přesuňte jej do jeho účtu
            session_cart_id = request.session.pop('cart_id', None)
            if session_cart_id:
                session_cart = Cart.objects.filter(id=session_cart_id).first()
                if session_cart:
                    # Přeneste obsah session cart (případně další logika)
                    session_cart.user = request.user
                    session_cart.save()
                    cart = session_cart  # Nastavte přenesený cart jako aktivní

            request.cart = cart
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
