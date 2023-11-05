from django.shortcuts import render, redirect, HttpResponseRedirect
from gerencia.models import Proveedor, Producto, Cliente, Categoria, Pedido, DetallePedido
from gerencia.forms import ProveedorForm



# Create your views here.
def index_gerencia(request):
    return render(request, 'gerencia/index.html')

def obtener_proveedor(request):
    proveedor = Proveedor.objects.filter(baja=False)

    if 'nombre' in request.GET:
        proveedor = proveedor.filter(nombre__contains=request.GET['nombre'])
    return render(request, 'gerencia/proveedor/index.html', {'proveedor': proveedor})
#Consulta sobre los proveedores que han sido dados de baja

def nuevo_proveedor(request):
    if request.method == "POST":
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
            except ValueError as ve: 
                formulario.add_error('nombre', str(ve))#lo saque del código subido del profe debo definir la variable ve
            else:
                return redirect('proveedor_index')
    else:
        formulario = ProveedorForm()
    return render(request, 'gerencia/proveedor/nuevo.html', {'form': formulario})
    #Valida si el formulario es valido