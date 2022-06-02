from django.db import models
from django.forms import IntegerField

# Create your models here.

class Articulos(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length= 30)
    descripcion = models.CharField(max_length= 40)
    seccion = models.CharField(max_length= 20)
    precio = models.IntegerField()
    stock = IntegerField()

class Cliente(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length= 40)
    direccion = models.CharField(max_length= 40)
    telefono = models.CharField(max_length= 15)

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    cliente = models.IntegerField()
    entregado = models.BooleanField()

class Ventas(models. Model):
    pedido = models.IntegerField()
    articulo = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()



