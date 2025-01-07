from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
]