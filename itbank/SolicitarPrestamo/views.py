from .models import Prestamo, Cuenta
from .serializers import PrestamoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
import json
# Create your views here.
class PrestamoLists(APIView):
    
    def get(self, request):
        prestamos = Prestamo.objects.all()
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
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