# forms.py
from django import forms
from .models import Cliente, Producto, Categoria

class PersonaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'})
    )

    apellido = forms.CharField(
        label='Apellido:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'})
    )

    email = forms.EmailField(
        label='Email:',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el email'})
    )

    dni = forms.IntegerField(
        label='DNI:',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el DNI'})
    )

    telefono = forms.CharField(
        label='Teléfono:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'})
    )

    class Meta:
        abstract = True

class ClienteForm(PersonaForm):
    direccion = forms.CharField(
        label='Dirección:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección'})
    )

    baja_cliente = forms.BooleanField(
        label='¿Cliente dado de baja?',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta(PersonaForm.Meta):
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'dni', 'telefono', 'direccion', 'baja_cliente']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['articulo', 'categoria', 'precio', 'marca', 'stock', 'proveedor', 'descripcion', 'imagen']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']