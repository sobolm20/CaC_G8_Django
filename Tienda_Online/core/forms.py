from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=30, required=True)
    apellido = forms.CharField(label="Apellido:", max_length=30, required=True)
    email = forms.EmailField(label="E-mail", required=True)
    telefono = forms.IntegerField(label="Número de teléfono", required=False)
    consulta = forms.CharField(label="Ingrese su consulta:",required=False, widget=forms.Textarea)