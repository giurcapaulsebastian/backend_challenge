from django.forms import ModelForm
from .models import Product, Nutrition

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'status']