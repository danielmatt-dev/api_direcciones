from abc import ABC, abstractmethod
from typing import List

from api_direcciones.core.entities.entities import Estado, Municipio, Colonia


class Mapper(ABC):

    @abstractmethod
    def to_list_entity_colonias(self, models) -> List[Colonia]:
        pass

    @abstractmethod
    def to_entity_estado(self, model) -> Estado:
        pass

    @abstractmethod
    def to_entity_municipio(self, model) -> Municipio:
        pass

    @abstractmethod
    def to_entity_colonia(self, model) -> Colonia:
        pass
