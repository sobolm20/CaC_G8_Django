#Formulario basado en clases
from django import forms

palabras_prohibidas = ['forro', 'pito', 'loca']

class ContactForm(forms.Form): #Los formularios basados en clases en Django se definen mediante la creación de una clase que hereda de la clase forms.Form.
    nombre = forms.CharField( #Los campos del formulario se definen como atributos de la clase del formulario. Cada campo corresponde a un elemento del formulario, como un cuadro de texto, un campo de fecha, etc
        label="Nombre:", 
        max_length=30, 
        required=True, 
        error_messages={'required': 'Por favor, complete el campo'},
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese aquí su nombre'})
    )
    apellido = forms.CharField(
        label="Apellido:", 
        max_length=30, 
        required=True,
        error_messages={'required': 'Por favor, complete el campo'},
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese aquí su apellido'})
    )
    email = forms.EmailField(
        label="E-mail", 
        required=True, 
        error_messages={'required': 'Por favor, complete el campo'}, 
        widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'xx@yy.zz'})
    )
    telefono = forms.IntegerField(
        label="Número de teléfono", 
        required=False
    )
    consulta = forms.CharField(
        label="Ingrese su consulta:", 
        required=False, 
        widget=forms.Textarea(attrs={'rows': 7, 'placeholder': 'Ingrese aquí su consulta'})
    )
    
    def contiene_prohibidas(self, valor):
        for palabra in palabras_prohibidas:
            if palabra.lower() in valor.lower():
                raise forms.ValidationError('El campo contiene palabras groseras o inapropiadas.')
        
    def clean(self):
        cleaned_data = super().clean() #La validación de datos se maneja mediante métodos de la clase del formulario, como clean_<campo>() para validar un campo específico o clean() para validar el formulario en su conjunto.
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        
        self.contiene_prohibidas(nombre)
        self.contiene_prohibidas(apellido)
        
        return cleaned_data
