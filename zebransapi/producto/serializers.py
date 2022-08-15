from rest_framework import serializers
from .models import Producto
from django.contrib.auth.models import User


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id', 'username', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}
        
        
        
        
        


