from rest_framework import serializers
from .models import Sucursal

class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"


