from abc import ABC, abstractmethod

from api_direcciones.infraestructure.delivery.dto.response.direccion import Direccion


class MapperDto(ABC):

    @abstractmethod
    def to_direccion(self, entities) -> Direccion:
        pass


class MapperDtoImpl(MapperDto):

    def to_direccion(self, entities) -> Direccion:
        return Direccion(
            codigo_postal=str(entities[0].codigo_postal),
            colonias=[colonia.nombre for colonia in entities],
            estado=entities[0].municipio.estado.nombre,
            ciudad=entities[0].ciudad,
            asentamiento=entities[0].asentamiento,
            pais=entities[0].municipio.estado.pais
        )
