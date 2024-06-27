from dataclasses import dataclass
from rest_framework import serializers
from typing import List


@dataclass
class Direccion:
    codigo_postal: str
    colonias: List[str]
    estado: str
    ciudad: str
    asentamiento: str
    pais: str


class DireccionSerializer(serializers.Serializer):
    codigo_postal = serializers.CharField(max_length=5)
    colonias = serializers.ListField(child=serializers.CharField(max_length=100))
    estado = serializers.CharField(max_length=50)
    ciudad = serializers.CharField(max_length=50)
    asentamiento = serializers.CharField(max_length=25)
    pais = serializers.CharField(max_length=10)
