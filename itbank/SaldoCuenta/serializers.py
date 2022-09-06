from rest_framework import serializers
from .models import TipoCliente
from .models import Cuenta


class TipoClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoCliente
        fields = 'type_name',

class SaldoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = 'balance',