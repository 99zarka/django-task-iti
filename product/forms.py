from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'quantity']
        help_texts = {
            'name': 'Enter the name of the product.',
            'price': 'Enter the price of the product.',
            'image': 'Upload an image for the product.',
            'quantity': 'Enter the available quantity of the product.',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
