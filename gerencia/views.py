from django.shortcuts import render
from typing import Any
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  #conjunto de vistas genéricas que son implementaciones comunes de patrones de visualización. Estas vistas permiten realizar operaciones CRUD 
from django.http import HttpRequest
from .models import Cliente, Producto, Categoria
from django.urls import reverse_lazy #Aca utilizamos reverse_lazy porque como estamos consultando en la BDD, solo la llamaremos cuando este todo listo cargado y validado. 
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required(login_url="login")
def indexG(request):
    return render(request, "gerencia\indexGerencia.html")

class ClienteListView(ListView):
    model = Cliente  # Con model debo decirle cual es el modelo del que debo tomar los campos
    context_object_name = 'clientes'
    template_name = 'gerencia/cliente/cliente_listar.html' #Cual es la pagina donde lo va a mostrar o cargar
    queryset = Cliente.objects.filter(baja = False)
    ordering = ['apellido']
        # esta vista muestra una lista de clientes, inicialmente filtrados para excluir aquellos con baja igual a True, y permite realizar búsquedas adicionales por apellido mediante parámetros GET.
    def get(self, request: HttpRequest, *args:Any, **kwargs:Any):  #Este método se utiliza para manejar las solicitudes GET. En este caso, se está personalizando para filtrar la lista de clientes según el apellido proporcionado en los parámetros de la solicitud.
        if 'apellido' in request.GET:
            self.queryset=self.queryset.filter(nombre__contains=request.GET['apellido'])
        return super().get(request, *args,**kwargs)  # se llama al método get de la clase base (super()) para realizar el procesamiento adicional necesario para obtener y renderizar la lista de objetos Cliente.

class ClienteDetailView(DetailView):#Fijate que no hereda siempre igual, dependiendo la funcion que va a realizar es lo que necesito que herede
    model = Cliente
    template_name = 'gerencia/cliente/cliente_detalle.html'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'gerencia/cliente/cliente_crear.html'
    fields = '__all__'
    success_url = reverse_lazy()

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'gerencia/cliente/cliente_actualizar.html'
    fields ='__all__'
    success_url = reverse_lazy('gerencia/cliente/cliente_listar.html')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_borrar.html'
    success_url = reverse_lazy('gerencia/cliente/cliente_listar.html')
    

#Falta terminar las vistas con la lógica de negocio


class ProductoListView(ListView):
    model = Producto
    template_name = 'gerencia/productos/producto_index.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'gerencia/productos/crear_producto.html' 
    success_url = reverse_lazy('producto_index')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'gerencia/productos/editar_producto.html'
    success_url = reverse_lazy('producto_index')
    
class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'gerencia/productos/eliminar_producto.html'
    success_url = reverse_lazy('producto_index')


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'gerencia/categoria/crear_categoria.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_categorias')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'gerencia/categoria/lista_categorias.html'
    context_object_name = 'categorias'
    
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'gerencia/categoria/actualizar_categoria.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_categorias')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'gerencia/categoria/eliminar_categoria.html'
    success_url = reverse_lazy('lista_categorias')