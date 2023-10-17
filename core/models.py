from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Categoria')
    baja = models.BooleanField(default=False)    
    

class Producto(models.Model):
    articulo = models.CharField(verbose_name="Articulo", max_length=50)
    imagen = models.ImageField(verbose_name="Imagen", max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.CharField(verbose_name="Precio", max_length=25)
    marca = models.CharField(verbose_name="Marca", max_length=25)
    stock = models.IntegerField(verbose_name="Stock")
    proveedor = models.CharField(verbose_name="Proveedor", max_length=250)
    descripcion = models.TextField(verbose_name="Descripcion", max_length=250)


