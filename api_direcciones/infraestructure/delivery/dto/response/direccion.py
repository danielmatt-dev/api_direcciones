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


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
