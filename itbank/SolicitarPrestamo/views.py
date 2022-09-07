from .models import Prestamo, Cuenta
from .serializers import PrestamoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
class PrestamoLists(LoginRequiredMixin, APIView):
    
    def get(self, request, pk):
        user = User.objects.get(username = User.get_username(request.user))
        if user.is_staff == True:
            prestamos = Prestamo.objects.all()
            serializer = PrestamoSerializer(prestamos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        user = User.objects.get(username = User.get_username(request.user))
        if user.is_staff == True:
            jd = request.data
            print(jd)
            cuenta = Cuenta.objects.get(customer_id = jd['customer_id'] )
            print(cuenta.balance)
            cuenta.balance = cuenta.balance + jd['loan_total']
            cuenta.save()
            print(cuenta.balance)
            serializer = PrestamoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = User.objects.get(username = User.get_username(request.user))
        if user.is_staff == True:
            prestamo = Prestamo.objects.filter(loan_id=pk).first()
            cuenta = Cuenta.objects.get(customer_id = prestamo.customer_id)
            print(cuenta.balance)
            cuenta.balance = cuenta.balance - prestamo.loan_total
            cuenta.save()
            print(cuenta.balance)
            if prestamo:
                serializer = PrestamoSerializer(prestamo)
                prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
     
    # DatosCliente = Cliente.objects.get(customer_name = User.get_username(request.user))
    #    if user.is_staff == False: