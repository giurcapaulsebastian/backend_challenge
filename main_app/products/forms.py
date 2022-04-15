from django import forms
from .models import Product, Nutrition

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'status']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
        }

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = '__all__'

        widgets = {
            'name' : forms.Select(attrs={'class': 'form-control'}),
            'unit' : forms.Select(attrs={'class': 'form-control'}),
            'product' : forms.Select(attrs={'class': 'form-control'}),
            'value' : forms.TextInput(attrs={'class': 'form-control'}),
        }