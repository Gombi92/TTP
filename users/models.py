from django.conf import settings
from products.models import Product
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,  # Povolit null
        blank=True  # Povolit prázdné hodnoty
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

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Muž'), ('female', 'Žena'), ('other', 'Jiné')],
        blank=True,
        null=True
    )
    communication_preference = models.CharField(
        max_length=10,
        choices=[('formal', 'Vykání'), ('informal', 'Tykání')],
        blank=True,
        null=True
    )


class UserFormSubmission(models.Model):
    GENDER_CHOICES = [
        ('male', 'Muž'),
        ('female', 'Žena'),
        ('other', 'Jiné'),
    ]

    NAME_CHOICES = [
        ('tykani', 'Tykání'),
        ('vykani', 'Vykání'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    formal_choice = models.CharField(max_length=10, choices=NAME_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

