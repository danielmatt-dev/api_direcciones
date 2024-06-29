from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api_direcciones.infraestructure.delivery.dto.request.codigo_postal import CodigoPostalSerializer
from api_direcciones.infraestructure.delivery.dto.request.usuario_serializer import UsuarioSerializer
from api_direcciones.infraestructure.delivery.dto.response.auth_token import AuthSerializer
from api_direcciones.infraestructure.delivery.dto.response.direccion import DireccionSerializer


@api_view(['POST'])
def crear_usuario(request, verificar_usuario, crear_cuenta, mapper_dto):
    user_serializer = UsuarioSerializer(data={request.data})
    if not user_serializer.is_valid():
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if verificar_usuario.execute(user_serializer.username):
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

    token = crear_cuenta.execute(mapper_dto.to_usuario)
    auth_token = mapper_dto.to_auth_token(token)
    auth_serializer = AuthSerializer(auth_token)

    return Response(auth_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_direcciones(request, codigo_postal: str, buscar_colonias, mapper_dto):

    serializer = CodigoPostalSerializer(data={'codigo_postal': codigo_postal})
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    colonias = buscar_colonias.execute(int(codigo_postal))
    if not colonias:
        return Response({'error': 'No se encontraron colonias'}, status=status.HTTP_404_NOT_FOUND)

    direccion = mapper_dto.to_direccion(colonias)
    serializer = DireccionSerializer(direccion)
    return Response(serializer.data, status=status.HTTP_200_OK)
