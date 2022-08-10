from django.db import models

# modelos.

class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=4, decimal_places=2)
    Disponibles = models.IntegerField(blank=True, null=True)
    Sku = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Nombre
    