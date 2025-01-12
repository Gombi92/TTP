from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    # Povinná pole
    email = forms.EmailField(required=True, help_text="Zadejte platnou e-mailovou adresu.")
    username = forms.CharField(required=True, help_text="Zadejte uživatelské jméno.")
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label="Heslo")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Potvrzení hesla")

    # Nepovinná pole
    first_name = forms.CharField(required=False, label="Jméno")
    last_name = forms.CharField(required=False, label="Příjmení")
    address = forms.CharField(required=False, label="Adresa")
    phone = forms.CharField(required=False, label="Telefon")
    gender = forms.ChoiceField(
        required=False,
        label="Pohlaví",
        choices=[
            ('male', 'Muž'),
            ('female', 'Žena'),
            ('nonbinary', 'Nebinární'),
        ]
    )
    communication_preference = forms.ChoiceField(
        required=True,  # Nastaveno jako povinné
        label="Tykání/Vykání",
        choices=[
            ('tykani', 'Tykání'),
            ('vykani', 'Vykání'),
        ],
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = (
            "username", "email", "password1", "password2", "first_name", "last_name", "address", "phone", "gender",
            "communication_preference")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        # Uloží další pole do uživatele, pokud to potřebuješ (rozšíření modelu User pomocí profilů apod.)
        if commit:
            user.save()
        return user
