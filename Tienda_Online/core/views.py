from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse
import json
from core.forms import ContactForm


# Create your views here.
def index(request):
    with open('static/productos.json','r',encoding='utf-8') as json_file:
        productos=json.load(json_file)

    # Extraer todas las categorías únicas de los productos
        categorias = set(producto['categoria'] for producto in productos)

        return render(request, "index.html", {'productos':productos,'categorias':categorias})

def contact(request):
    if request.method == "GET":
        formulario_contacto = ContactForm()
        # respuesta=""
    elif request.method == "POST":
        formulario_contacto = ContactForm(request.POST)
        if formulario_contacto.is_valid():
            # respuesta=f"Mensaje recibido. Agradecemos su consulta."
            return redirect(reverse('index'))
    else:
        return HttpResponseBadRequest ("Método no correcto")
    
    contexto={
        # 'respuesta': respuesta,
        'formulario': formulario_contacto,
    }
        
        
    return render(request, "contact.html", contexto)



def details(request, producto_id):
    # Ruta al archivo JSON que contiene la información de los productos
    json_file_path = 'static/productos.json'  # Reemplaza con la ruta correcta
    
    # Carga el archivo JSON
    with open(json_file_path, 'r') as json_file:
        productos_data = json.load(json_file)
    
    # Busca el producto con el ID proporcionado
    producto = None
    for prod in productos_data:
        if prod['id'] == int(producto_id):
            producto = prod
            break
    
    # Si no se encontró el producto, muestra un error 404
    if producto is None:
        raise Http404("Producto no encontrado")
    
    return render(request, 'Details.html', {'producto': producto})
