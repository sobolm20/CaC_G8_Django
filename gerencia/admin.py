from django.contrib import admin
from gerencia.models import Producto, Categoria, Proveedor,Cliente
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Cliente)