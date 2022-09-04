from rest_framework import serializers
from .models import Prestamo

class PrestamosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"


