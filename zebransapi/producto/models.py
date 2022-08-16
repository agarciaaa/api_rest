from django.db import models
from django.contrib.auth.models import User

# modelos.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    anonimo = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.user



class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Marca = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=4, decimal_places=2)
    Disponibles = models.IntegerField(blank=True, null=True)
    Sku = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default= 0)
    
    def __str__(self):
        return self.Nombre
    


