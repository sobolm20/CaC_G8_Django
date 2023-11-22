from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100, blank=False)
    apellido = models.CharField(verbose_name='Apellido', max_length=150, blank=False)
    email = models.EmailField(verbose_name='Email', max_length=150, blank=False, null=True)
    dni = models.IntegerField(verbose_name="DNI")
    telefono= models.CharField(verbose_name="Teléfono", max_length=50)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.dni} - {self.nombre} - {self.apellido}"
    

class Proveedor(Persona):
    empresa = models.CharField(verbose_name="Empresa", max_length=100)
    categoria = models.CharField(verbose_name="Categoría", max_length=50)
    cuit = models.CharField(verbose_name="CUIT/Cuil", max_length=20)
    localidad = models.CharField(verbose_name="Localidad", max_length=250)
    baja_proveedor = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Proveedores'
        
    def __str__(self):
        return f"{self.empresa} - {self.cuit} - {self.telefono}"
    
    def soft_delete(self):
        self.baja_proveedor = True #Damos de baja un proveedor sin eliminar sus datos de la base de datos
        super().save() #Guardamos los cambios en la base de datos

    def restore(self):
        self.baja_proveedor =True #Restauramos el estado del proveedor a activo
        super().save() #Guardamos los cambios en la base de datos

class Cliente(Persona):
    direccion = models.CharField(verbose_name='Dirección', max_length=200)
    baja = models.BooleanField(default=False) 
    #metodos_pago
    #historial_pedido
    #notificacion   Como no se como manejarlas las pongo como idea
    #reseñas
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.dni} - {self.direccion}"
    def soft_delete(self):
        self.baja = True #Damos de baja un proveedor sin eliminar sus datos de la base de datos
        super().save()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Categoria')
    baja = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    articulo = models.CharField(verbose_name="Artículo", max_length=50)
    imagen = models.ImageField(verbose_name="Imagen", max_length=250, upload_to='img', null=True, blank=True) #upload especifica la carpeta donde encontrar las imagenes
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.CharField(verbose_name="Precio", max_length=25)
    marca = models.CharField(verbose_name="Marca", max_length=25)
    stock = models.IntegerField(verbose_name="Stock")
    proveedor = models.ManyToManyField(Proveedor)
    descripcion = models.TextField(verbose_name="Descripción", max_length=250)


class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name="Total", max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido #{self.id} - {self.fecha_pedido}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Detalle de Pedido'
    def __str__(self):
        return f'Detalle de Pedido #{self.pedido.id} - {self.producto.nombre}'
