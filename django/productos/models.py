from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: eliminar el producto
    # PROTECT: lanza un error
    # RESTRICT: solo elimina si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna un valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)