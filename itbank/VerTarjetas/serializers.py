from rest_framework import serializers
from .models import Tarjeta

class TarjetasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"


