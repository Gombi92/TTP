from django import forms
from .models import UserFormSubmission, CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'address', 'phone', 'gender', 'communication_preference']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Uživatelské jméno', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Heslo', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Adresa', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'communication_preference': forms.Select(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        }),
        label="E-mail"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Heslo'
        }),
        label="Heslo"
    )
