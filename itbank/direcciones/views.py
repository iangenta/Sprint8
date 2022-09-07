from .models import Direccion, Cliente
from .serializers import direccionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from pprint import pprint

class DireccionF(LoginRequiredMixin, APIView):
    
    def get(self, request, pk):
        DatosCliente = Cliente.objects.get(customer_name = User.get_username(request.user))
        
        user = User.objects.get(username = User.get_username(request.user))
        if user.is_staff == False:
            pk = DatosCliente.customer_address_id
            
        direccionCliente = Direccion.objects.get(address_id = pk)
        serializer = direccionSerializer(direccionCliente)
        if direccionCliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        
        DatosCliente = Cliente.objects.get(customer_name = User.get_username(request.user))
        
        user = User.objects.get(username = User.get_username(request.user))
        if user.is_staff == False:
            pk = DatosCliente.customer_address_id
        
        direccionCliente = Direccion.objects.get(address_id = pk)
        serializer = direccionSerializer(direccionCliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#user = User.objects.get(username = User.get_username(request.user))
#if user.is_staff == True:





""" def get(self, request, pk):
        direccionCliente = Direccion.objects.get(address_id = pk)
        serializer = direccionSerializer(direccionCliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND) """