from abc import ABC, abstractmethod
from typing import List

from api_direcciones.core.entities.entities import Colonia
from api_direcciones.infraestructure.delivery.dto.response.direccion import Direccion


class MapperDto(ABC):

    @abstractmethod
    def to_direccion(self, entities) -> Direccion:
        pass


class MapperDtoImpl(MapperDto):

    def to_direccion(self, entities: List[Colonia]) -> Direccion:
        return Direccion(
            codigo_postal=str(entities[0].codigo_postal),
            colonias=dict(zip([entity.nombre for entity in entities], [entity.asentamiento for entity in entities])),
            estado=entities[0].municipio.estado.nombre,
            ciudad=entities[0].ciudad,
            pais=entities[0].municipio.estado.pais
        )
