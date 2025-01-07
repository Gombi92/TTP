from .models import Cart

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Základní logika middleware
        if not request.user.is_authenticated:
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
        else:
            cart, _ = Cart.objects.get_or_create(user=request.user)
            request.cart = cart

        response = self.get_response(request)
        return response