from .models import AuthUser
from .serializers import TarjetasSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarjeta
# Create your views here.

class TarjetasList(APIView):
    def get(self, request, pk):
        Tarjetas = Tarjeta.objects.filter(pk=pk)
        serializer = TarjetasSerializers(Tarjetas, many = True)
        if Tarjetas:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


