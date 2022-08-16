from functools import partial
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets 
from .serializers import ProductoSerializer
from .serializers import UsuarioSerializer
from .models import Producto
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth.models import User
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)
from django.conf import settings
from rest_framework import serializers

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer 
    permission_classes = [IsAuthenticated]

    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def consulta_vista(self, producto):
        num = producto.count
        num = num + 1
        producto.count = num
        producto.save()
        
    def list(self, request):
        productos = Producto.objects.all()
        for producto in productos:
            self.consulta_vista(producto)
        serializer = ProductoSerializer(productos, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    def retrieve(self, request, pk=None):
        try:
            producto = Producto.objects.get(pk=self.kwargs.get("pk"))
        except:
            return HttpResponse(status=404)
        self.consulta_vista(producto)
        serializer = ProductoSerializer(producto)
        
        return JsonResponse(serializer.data, safe=False)



       
    def update(self, request, pk=None):
        try:
            producto = Producto.objects.get(pk=self.kwargs.get("pk"))
        except:
            return HttpResponse(status=400)
        
        serializer = ProductoSerializer(producto, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        usuario = self.request.user.username
        remitente = []
        users = User.objects.all()
        for user in users:
            try: 
                remitente.append(user.email)
            except:
                pass

        
        context = {'nombre': producto.Nombre, 'modificado': producto.modificado, 'usuario': usuario}
        
        Mail.send(remitente, context)
        #return HttpResponse(status=200)
        return JsonResponse(serializer.data, safe=False)

        
       
class Mail():

    def send(remitente, context):
        template = get_template('email.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'Producto Modificado',
            'Admin Modificacion de Producto',
            settings.EMAIL_HOST_USER,
            remitente
        )
        email.attach_alternative(content, 'text/html')
        email.send()
