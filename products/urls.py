from django.urls import path
from . import views
from .views import product_detail


urlpatterns = [
    path('', views.products, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
