from django.core.validators import RegexValidator
from rest_framework import serializers


class CodigoPostalSerializer(serializers.Serializer):

    codigo_postal = serializers.CharField(
        min_length=5,
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^\d{5}$',
                message='El código postal debe ser un número de 5 dígitos'
            )
        ]
    )
