from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
#les decimos cuales son los de solo lectura
#read_only_fields = ("id","created_at","updated_at",)


