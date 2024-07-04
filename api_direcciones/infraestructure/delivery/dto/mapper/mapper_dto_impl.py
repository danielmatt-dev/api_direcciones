from typing import List

from api_direcciones.core.entities.entities import Colonia, Usuario
from api_direcciones.infraestructure.delivery.dto.mapper.mapper_dto import MapperDto
from api_direcciones.infraestructure.delivery.dto.response.auth_token import AuthToken
from api_direcciones.infraestructure.delivery.dto.response.direccion import Direccion, ColoniaDto


class MapperDtoImpl(MapperDto):

    def to_direccion(self, entities: List[Colonia]) -> Direccion:
        return Direccion(
            codigo_postal=str(entities[0].codigo_postal),
            colonias=[ColoniaDto(nombre=colonia.nombre, tipo=colonia.asentamiento) for colonia in entities],
            estado=entities[0].municipio.estado.nombre,
            ciudad=entities[0].ciudad,
            pais=entities[0].municipio.estado.pais
        )

    def to_usuario(self, data) -> Usuario:
        return Usuario(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )

    def to_auth_token(self, token) -> AuthToken:
        return AuthToken(
            refresh=str(token),
            access=str(token.access_token)
        )
