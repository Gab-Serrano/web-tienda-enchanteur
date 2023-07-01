from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)

    class Meta:
        
        model = Product
        fields = ['name', 'description', 'price', 'image']