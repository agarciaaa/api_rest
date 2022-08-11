import imp
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import Producto


# Create your views here.


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()