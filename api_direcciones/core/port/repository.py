from abc import ABC, abstractmethod
from typing import List
from rest_framework_simplejwt.tokens import Token

from api_direcciones.core.entities.entities import Colonia


class Repository(ABC):

    @abstractmethod
    def buscar_colonias_por_codigo_postal(self, codigo_postal: int) -> List[Colonia]:
        pass

    @abstractmethod
    def verificar_existencia_usuario(self, username) -> bool:
        pass

    @abstractmethod
    def crear_usuario(self, usuario) -> Token:
        pass
