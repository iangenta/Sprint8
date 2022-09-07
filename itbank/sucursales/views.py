from .models import Sucursal
from .serializers import SucursalesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SucursalList(APIView):

    def get(self, request): # nuevo
        Sucursales = Sucursal.objects.all()
        serializer = SucursalesSerializer(Sucursales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)