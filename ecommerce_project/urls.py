from django.contrib import admin
from django.urls import path
from . import views  # Importuje views z hlavního souboru views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Hlavní URL povede na funkci home
    path('products/', views.products, name='products'),  # Stránka se zbožím
    path('login/', views.login_view, name='login'),  # Add login view
    path('register/', views.register_view, name='register'),  # Add register view
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]