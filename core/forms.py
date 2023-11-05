from typing import Any
from django import forms
from django.forms import ValidationError
from core.models import Categoria, Proveedor, Producto


palabras_prohibidas=['forro','pito', 'loca']

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre:", 
        max_length=30, 
        required=True, 
        error_messages={'required': 'Por favor, complete el campo'},
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí su nombre'}))
    apellido = forms.CharField(
        label="Apellido:", 
        max_length=30, 
        required=True,
        error_messages={'required': 'Por favor, complete el campo'},
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí su apellido'}))
    email = forms.EmailField(
        label="E-mail", 
        required=True, 
        error_messages={'required': 'Por favor, complete el campo'}, 
        widget=forms.EmailInput(attrs={'type': 'email','placeholder':'xx@yy.zz'}))
    telefono = forms.IntegerField(
        label="Número de teléfono", 
        required=False)
    consulta = forms.CharField(
        label="Ingrese su consulta:", 
        required=False, 
        widget=forms.Textarea(attrs={'rows': 7, 'placeholder':'Ingrese aquí su consulta'}))
    
    def contiene_prohibidas(self, valor):
         for palabra in palabras_prohibidas:
            if palabra.lower() in valor.lower():
                raise forms.ValidationError('El campo contiene palabras groseras o inapropiadas.')
        
    def clean_nombre(self):
        valor = self.cleaned_data.get('nombre')
        self.contiene_prohibidas(valor)
        return valor
    
    def clean_apellido(self):
        valor = self.cleaned_data.get('apellido')
        self.contiene_prohibidas(valor)
        return valor
    
class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        label = 'Nombre: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí la categoría'})
    )
    class Meta:
        model=Categoria
        fields=['nombre']


class ProveedorForm(forms.ModelForm):
    proveedor = forms.CharField(
        label = 'Proveedor: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí la Razón Social'})
    )
    direccion = forms.CharField(
        label = 'Dirección: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí la descripción'})
    )
    localidad = forms.CharField(
        label = 'Localidad: ',
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí la localidad'})
    )
    telefono = forms.CharField(
        label = 'Teléfono: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí el teléfono de contacto'})
    )
    mail = forms.CharField(
        label = 'E-mail: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí un email de contacto'})
    )

    class Meta:
        model = Proveedor
        fields = ['proveedor','direccion','localidad','telefono','mail']


class ProductoForm(forms.ModelForm):
    articulo = forms.CharField(
        label = 'Artículo: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí el artículo'})
    )
    imagen = forms.URLField(
        label = 'Link a la imagen: ',
        required = True,
        widget=forms.URLInput(attrs={'placeholder':'Ingrese aquí un link a la imagen'})
    )
    categoria = forms.CharField(
        label = 'Categoria: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí la categoria'})
    )
    precio = forms.FloatField(
        label = 'Precio: ',
        required = True,
        widget=forms.NumberInput(attrs={'placeholder':'Ingrese aquí el precio unitario'})
    )
    marca = forms.CharField(
        label = 'Marca: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí la marca del artículo'})
    )
    stock = forms.IntegerField(
        label = 'Stock: ',
        widget=forms.NumberInput(attrs={'placeholder':'Ingrese aquí la cantidad en stock'})
    )
    proveedor = forms.CharField(
        label = 'Proveedor: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí el proveedor'})
    )
    descripcion = forms.Textarea(
        label = 'Descripción: ',
        required = True,
        widget=forms.TextInput(attrs={'placeholder':'Ingrese aquí un email de contacto'})
    )

    class Meta:
        model = Producto
        fields = ['articulo','imagen','categoria','precio','marca','stock','proveedor','descripcion']
