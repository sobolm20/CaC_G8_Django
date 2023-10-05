from django import forms

palabras_prohibidas=['forro','pito', 'laca']
class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=30, required=True)
    apellido = forms.CharField(label="Apellido:", max_length=30, required=True)
    email = forms.EmailField(label="E-mail", required=True)
    telefono = forms.IntegerField(label="Número de teléfono", required=False)
    consulta = forms.CharField(label="Ingrese su consulta:",required=False, widget=forms.Textarea)
    def contiene_prohibidas(valor):
         for palabra in palabras_prohibidas:
            if palabra.lower() in valor.lower():
                raise forms.ValidationError('El campo contiene palabras groseras o inapropiadas.')
    
    def clean_nombre(self):
        valor = self.cleaned_data.get('nombre')
        self.contiene_prohibidas(valor)
        return valor