from abc import ABC, abstractmethod
from typing import List

from api_direcciones.core.entities.entities import Colonia


class Repository(ABC):

    @abstractmethod
    def buscar_colonias_por_codigo_postal(self, codigo_postal: int) -> List[Colonia]:
        pass
