from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .serializers import UsuarioSerializer
from .models import Producto
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

# Create your views here.

# queryset = User.objects.all()  como solicitar todos los usuarios

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer 

    #........


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer 

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        metodos = ['update','create','delete']

        if self.action in metodos:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]

    '''def list(self, request):
        
        return JsonResponse(self, safe=False)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass



        Mail.send(remitente, context)
        return super(ProductEdit, self).form_valid(form)
        '''

class Mail():

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