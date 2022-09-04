from .models import AuthUser
from .serializers import TarjetasSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarjeta
from pprint import pprint
from django.contrib.auth.models import User
# Create your views here.

class TarjetasList(APIView):
    def get(self, request, customer_id):
        Usuario = User.objects.filter((request))
        pprint(vars(Usuario))
        Tarjetas = Tarjeta.objects.filter(customer_id=customer_id)
        serializer = TarjetasSerializers(Tarjetas, many = True)
        if Tarjetas:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


