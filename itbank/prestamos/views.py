from .models import Prestamo
from .models import Cliente
from .serializers import PrestamoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from pprint import pprint

class PrestamoDetails(LoginRequiredMixin, APIView):
     
    def get(self, request):
        
        ClienteAutenticado = Cliente.objects.get(customer_name = User.get_username(request.user))
        DatosPrestamo = Prestamo.objects.filter(customer_id = ClienteAutenticado.customer_id)
        #pprint(vars(DatosPrestamo))
        #DatosCliente = Cliente.objects.filter(pk=pk).first()
        
        serializer = PrestamoSerializer(DatosPrestamo, many = True)
        
        if DatosPrestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

""" def get(self, request): # nuevo
        Usuarios = AuthUser.objects.all().order_by('created_at')
        serializer = AuthUserSerializer(Usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) """