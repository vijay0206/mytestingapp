from django import forms

from .models import Product

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()