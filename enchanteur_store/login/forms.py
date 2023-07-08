from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomPasswordInput(forms.PasswordInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control', 'placeholder': 'Contraseña', 'required': 'True', 'autocomplete': 'off'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',widget=CustomPasswordInput()
        )
    password2 = forms.CharField(
        label='Confirmar contraseña',widget=CustomPasswordInput()
        )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-floating datepicker', 'type': 'date'}),
        required=True
    )
    phone = forms.CharField(max_length=20, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")'})
        )
    address = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'required': 'True'})
        )
    city = forms.CharField(max_length=20, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad', 'required': 'True'})
        )
    country = forms.CharField(max_length=20, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País', 'required': 'True'})
        )
    state = forms.CharField(max_length=20, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado', 'required': 'True'})
        )
    zip_code = forms.CharField(max_length=20, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código postal', 'required': 'True'})
        )    

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1','password2', 'address', 'phone', 'city', 'state', 'zip_code', 'country', 'date_of_birth')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario', 'required': 'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'required': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': 'True'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'required': 'True'}),
        }
