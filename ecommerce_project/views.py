from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')