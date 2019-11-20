from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    dni_cliente = models.IntegerField()
    nombre_cliente = models.CharField(max_length = 120)
    apellidos_cliente = models.CharField(max_length = 120)
    correo_cliente = models.CharField(max_length = 120)
    def __str__(self):
        return self.nombre_cliente+' '+self.apellidos_cliente
class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre_admin = models.CharField(max_length=120)
    contrasenia_admin = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_admin
class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    descripcion_cita = models.TextField()
    fecha_cita = models.DateTimeField()
    id_cli_cita = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion_cita
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion_producto = models.TextField()
    nombre_producto = models.CharField(max_length=280)
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='productos_imagenes')
    def __str__(self):
        return self.nombre_producto
