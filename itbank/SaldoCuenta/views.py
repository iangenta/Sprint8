from .models import Cliente, TipoCliente, Cuenta
from .serializers import TipoClienteSerializers, SaldoSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class SaldoCuenta(APIView, LoginRequiredMixin):
    def get(self, request):
        
        ClienteAutenticado = Cliente.objects.get(customer_name = User.get_username(request.user)) #captura cliente
        
        tipo_cliente = TipoCliente.objects.get(customer_type_id = ClienteAutenticado.customer_type_id)
        saldo = Cuenta.objects.get(customer_id = ClienteAutenticado.customer_id)
        
        serializer = SaldoSerializers(saldo)
        serializer2 = TipoClienteSerializers(tipo_cliente)
        if ClienteAutenticado:
            return Response((serializer.data, serializer2.data), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
