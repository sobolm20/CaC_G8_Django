from django import forms
from django.forms import ValidationError
from gerencia.models import Proveedor, Producto, Cliente, Categoria, Pedido, DetallePedido

class ProveedorForm(forms.ModelForm): #se usará para crear, editar y validar instancias del modelo Proveedor
    
    class Meta: # la clase Meta se utiliza para proporcionar metainformación sobre el formulario. En este caso, Meta se usa para configurar cómo se debe generar el formulario a partir del modelo Proveedor
        model = Proveedor
        fields =['nombre', 'apellido', 'empresa', 'cuit', 'localidad', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'cuit': forms.TextInput(attrs={'class':'form-contro'}),
            'localidad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
        }