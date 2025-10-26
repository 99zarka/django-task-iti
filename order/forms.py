from django import forms
from .models import Order
from product.models import Product
from django.core.exceptions import ValidationError

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'email', 'product', 'product_quantity']
        help_texts = {
            'address': 'Enter your shipping address.',
            'email': 'Enter your email address for order confirmation.',
            'product': 'Select the product you wish to order.',
            'product_quantity': 'Enter the quantity of the product you want to order.',
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def clean_product_quantity(self):
        product_quantity = self.cleaned_data['product_quantity']
        product = self.cleaned_data['product']

        if product_quantity <= 0:
            raise ValidationError("Quantity must be a positive number.")

        if product.quantity < product_quantity:
            raise ValidationError(f"Only {product.quantity} units of {product.name} are available.")
        
        return product_quantity
