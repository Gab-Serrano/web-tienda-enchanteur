from django import forms
from store.models import Product
from django.forms import ClearableFileInput


class ProductForm(forms.ModelForm):
    #class Product(models.Model):
    #   name = models.CharField(max_length = 50, null=True)
    #   description = models.CharField(max_length = 200, null=True)
    #   price = models.IntegerField()
    #   image = models.ImageField(null=True, blank=True, upload_to='products-img/')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'featured']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto', 'required': 'True'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style':'height: 100px', 'placeholder': 'Ingrese la descripción del producto', 'required': 'True'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio del producto', 'required': 'True', 'min': '0'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox',}),
            'image': ClearableFileInput(attrs={'class': 'form-control', 'type':'file','accept': 'image/*', 'required': 'True'}),
        }
    
