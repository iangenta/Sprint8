from .models import Prestamo
from .serializers import PrestamosSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.

class PrestamoList(APIView):
    def get(self, request, branch_id):
        user = User.objects.get(username = User.get_username(request.user))
        prestamos = Prestamo.objects.filter(branch_id = branch_id)
        serializer = PrestamosSerializers(prestamos, many = True)
        if user.is_staff == True:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
