from abc import ABC, abstractmethod

from api_direcciones.core.entities.entities import Usuario
from api_direcciones.infraestructure.delivery.dto.response.auth_token import AuthToken
from api_direcciones.infraestructure.delivery.dto.response.direccion import Direccion


class MapperDto(ABC):

    @abstractmethod
    def to_direccion(self, entities) -> Direccion:
        pass

    @abstractmethod
    def to_usuario(self, serializer) -> Usuario:
        pass

    @abstractmethod
    def to_auth_token(self, token) -> AuthToken:
        pass
