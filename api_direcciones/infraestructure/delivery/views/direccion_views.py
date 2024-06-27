from injector import inject
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_direcciones.core.use_cases.buscar_colonias import BuscarColonias
from api_direcciones.infraestructure.delivery.dto.mapper.mapper_dto import MapperDto
from api_direcciones.infraestructure.delivery.dto.request.codigo_postal import CodigoPostalSerializer
from api_direcciones.infraestructure.delivery.dto.response.direccion import DireccionSerializer


class DireccionView(APIView):

    @inject
    def __init__(self, buscar_colonias: BuscarColonias, mapper_dto: MapperDto, **kwargs):
        super().__init__(**kwargs)
        self.buscar_colonias = buscar_colonias
        self.mapper_dto = mapper_dto

    def get(self, request, codigo_postal: int):

        serializer = CodigoPostalSerializer(data={'codigo_postal': codigo_postal})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        colonias = self.buscar_colonias.execute(codigo_postal)
        if not colonias:
            return Response({'error': 'No se encontraron colonias'}, status=status.HTTP_404_NOT_FOUND)

        direccion = self.mapper_dto.to_direccion(colonias)
        serializer = DireccionSerializer(direccion)
        return Response(serializer.data, status=status.HTTP_200_OK)
