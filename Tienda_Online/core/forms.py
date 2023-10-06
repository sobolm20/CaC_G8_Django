from typing import Any
from django import forms
from django.forms import ValidationError

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