import mailbox
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .serializers import UsuarioSerializer
from .models import Producto
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        usuario = serializer.save()
        usuario.set_password(usuario.password)
        usuario.save()
        return super().perform_create(serializer)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        Producto = serializer.save()
        Producto.set_password(Producto.password)
        Producto.save()
        return super().perform_create(serializer)

   

"""class Mail():

    def send(self, remitente, context):
        template = get_template('email.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'Product Modified',
            'Admin Modified Product',
            settings.EMAIL_HOST_USER,
            remitente
        )
        email.attach_alternative(content, 'text/html')
        email.send()
        
        
Mail.send(remitente, context)
return super(ProductEdit, self).form_valid(form)
"""