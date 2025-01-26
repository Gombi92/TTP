from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Heslo', 'class': 'form-control'}),
        label="Heslo",
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'address', 'phone', 'gender', 'communication_preference']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Uživatelské jméno', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Adresa', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'communication_preference': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        """Přepíše metodu save, aby hashovala heslo."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hashování hesla
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255, required=True)
    password = forms.CharField(label="Heslo", widget=forms.PasswordInput, required=True)
