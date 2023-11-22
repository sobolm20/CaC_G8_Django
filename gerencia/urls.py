from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ProductoListView, ProductoForm,ProductoCreateView,ProductoDeleteView,ProductoUpdateView, CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
from gerencia import views


urlpatterns = [
    path('', views.indexG, name='indexGerencia'),
    #Carga de urls del CRUD clientes
    path('cliente/',ClienteListView.as_view(), name='indexCliente' ),
    path('cliente/nuevo', ClienteCreateView.as_view(), name = 'nuevoCliente'),
    path('cliente/editar/<int:pk>', ClienteUpdateView.as_view(), name='editarCliente'),
    path('cliente/eliminar/<int:pk>',ClienteDeleteView.as_view(), name='eliminarCliente'),

    path('producto/', ProductoListView.as_view(), name='producto_index'),
    path('producto/nuevo', ProductoCreateView.as_view(), name='crearProducto'),
    path('producto/editar/<int:pk>', ProductoUpdateView.as_view(),name='editarProducto'),
    path('producto/eliminar/<int:pk>', ProductoDeleteView.as_view(), name='eliminarProducto'),

    path('categoria/', CategoriaListView.as_view(), name='lista_categorias'),
    path('categoria/nueva', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/editar/<int:pk>', CategoriaUpdateView.as_view(), name='actualizar_categoria'),
    path('categoria/eliminar/<int:pk>', CategoriaDeleteView.as_view(), name='eliminar_categoria'),
]