from django.conf import settings
from django.db import models
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.user.username if self.user else 'Anonymous'})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    size = models.CharField(max_length=3, choices=Product.SIZE_CHOICES, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        """Vypočítá celkovou cenu položky v košíku."""
        return self.product.sell_price * self.quantity

    def __str__(self):
        size_info = f" (Size: {self.size})" if self.size else ""
        return f"{self.product.name}{size_info}"
