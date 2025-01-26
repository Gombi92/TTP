
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()



def logout_view(request):
    logout(request)
    messages.success(request, 'Úspěšně jste se odhlásili!')
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')
