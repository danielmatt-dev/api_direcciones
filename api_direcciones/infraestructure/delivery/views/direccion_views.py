from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from api_direcciones.infraestructure.delivery.dto.request.codigo_postal import CodigoPostalSerializer
from api_direcciones.infraestructure.delivery.dto.response.direccion import DireccionSerializer


class DireccionView(APIView):

    def __init__(self, buscar_colonias, **kwargs):
        super().__init__(**kwargs)
        self.buscar_colonias = buscar_colonias

    def get(self, request):

        serializer = CodigoPostalSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        codigo_postal = serializer.validated_data['codigo_postal']
        colonias = self.buscar_colonias.execute(codigo_postal)

        if not colonias:
            return Response(serializer.errors, status=HTTP_404_NOT_FOUND)

        serializer = DireccionSerializer(colonias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
