from django.shortcuts import render
from django.http import Http404
import json


# Create your views here.
def index(request):
    with open('static/productos.json','r',encoding='utf-8') as json_file:
        productos=json.load(json_file)

    # Extraer todas las categorías únicas de los productos
        categorias = set(producto['categoria'] for producto in productos)

        return render(request, "index.html", {'productos':productos,'categorias':categorias})

def contact(request):
    return render(request, "contact.html")



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
