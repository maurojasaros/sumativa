from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='juegos')

    def __str__(self):
        return self.nombre
    
class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=50) 

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    direccion = models.TextField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Carrito de {self.usuario.nombre}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.juego.nombre} en carrito"

class Pedido(models.Model):
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Pedido realizado el {self.fecha_pedido}"