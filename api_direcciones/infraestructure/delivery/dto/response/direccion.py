from dataclasses import dataclass
from rest_framework import serializers
from typing import List


@dataclass
class ColoniaDto:
    nombre: str
    tipo: str


@dataclass
class Direccion:
    codigo_postal: str
    colonias: List[ColoniaDto]
    estado: str
    ciudad: str
    pais: str


class ColoniaDtoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    tipo = serializers.CharField(max_length=25)


class DireccionSerializer(serializers.Serializer):
    codigo_postal = serializers.CharField(max_length=5)
    colonias = ColoniaDtoSerializer(many=True)
    estado = serializers.CharField(max_length=50)
    ciudad = serializers.CharField(max_length=50)
    pais = serializers.CharField(max_length=10)
