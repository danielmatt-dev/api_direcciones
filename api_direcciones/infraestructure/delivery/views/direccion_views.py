from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_direcciones.infraestructure.delivery.dto.request.codigo_postal import CodigoPostalSerializer
from api_direcciones.infraestructure.delivery.dto.response.direccion import DireccionSerializer


@api_view(['GET'])
def get_direcciones(request, codigo_postal: int, buscar_colonias, mapper_dto):

    serializer = CodigoPostalSerializer(data={'codigo_postal': codigo_postal})
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    colonias = buscar_colonias.execute(codigo_postal)
    if not colonias:
        return Response({'error': 'No se encontraron colonias'}, status=status.HTTP_404_NOT_FOUND)

    direccion = mapper_dto.to_direccion(colonias)
    serializer = DireccionSerializer(direccion)
    return Response(serializer.data, status=status.HTTP_200_OK)
