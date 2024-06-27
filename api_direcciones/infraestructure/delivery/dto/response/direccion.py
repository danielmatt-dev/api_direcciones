from dataclasses import dataclass
from rest_framework import serializers
from typing import Dict


@dataclass
class Direccion:
    codigo_postal: str
    colonias: Dict[str, str]
    estado: str
    ciudad: str
    pais: str


class DireccionSerializer(serializers.Serializer):
    codigo_postal = serializers.CharField(max_length=5)
    colonias = serializers.DictField(child=serializers.CharField(max_length=100))
    estado = serializers.CharField(max_length=50)
    ciudad = serializers.CharField(max_length=50)
    pais = serializers.CharField(max_length=10)
