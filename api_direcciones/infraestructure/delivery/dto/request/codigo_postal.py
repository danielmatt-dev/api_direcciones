from rest_framework import serializers


class CodigoPostalSerializer(serializers.Serializer):

    codigo_postal = serializers.CharField(
        min_length=5,
        max_length=5,
        validators=[
            serializers.RegexField(
                regex=r'^\d{5}$',
                error_messages='El código postal debe ser un número de 5 dígitos'
            )
        ]
    )
