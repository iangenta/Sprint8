from .models import Cliente,Cuenta
from django.shortcuts import render
from .serializers import ClienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ClienteDetails(LoginRequiredMixin, APIView):
    
    def get(self, request):
        
        DatosCliente = Cliente.objects.get(customer_name = User.get_username(request.user))
        #pprint(vars(DatosCliente))
        #DatosCliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(DatosCliente)
        if DatosCliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@login_required

def index_clientes(request):

    usuario = Cliente.objects.get(customer_name = User.get_username(request.user))
    
    customerID = usuario.customer_id
    filtro_cuenta = Cuenta.objects.filter(customer_id=customerID)
    filtro_cliente = Cliente.objects.filter(customer_id=customerID)
    cuenta = filtro_cuenta.filter(account_id=filtro_cuenta[0].account_id)
    balance_final = cuenta[0].balance 
    clase= cuenta[0].account_type
    cliente =filtro_cliente.filter(customer_id=filtro_cliente[0].customer_id)
    tipo_cliente = cliente[0].customer_type
    cuenta.update(balance=balance_final)
    
    return render(request,'clientes/index.html',{'balance':balance_final, 'clase':clase,'tipo_cliente':tipo_cliente})
#usuario = Cliente.objects.get(customer_name = User.get_username(request.user))