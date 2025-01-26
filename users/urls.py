from django.urls import path
from . import views
from .views import user_form_view, register_view
from django.shortcuts import render


urlpatterns = [
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('register/', register_view, name='register'),
    path('form/', user_form_view, name='user_form'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('about/', views.about, name='about'),

]