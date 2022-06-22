from django import forms
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProducto','precio','stock','talla','catalogo']