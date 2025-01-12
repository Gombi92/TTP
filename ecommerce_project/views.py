from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm  # Importuj vlastní registrační formulář

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Úspěšně jste se přihlásili!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # Použij vlastní registrační formulář
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Úspěšně jste se zaregistrovali!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

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
