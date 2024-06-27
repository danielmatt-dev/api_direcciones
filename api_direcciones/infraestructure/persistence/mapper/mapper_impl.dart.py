from typing import List

from api_direcciones.core.entities.entities import Estado, Municipio, Colonia
from api_direcciones.infraestructure.persistence.mapper.mapper import Mapper


class MapperImpl(Mapper):

    def to_list_entity_estados(self, models) -> List[Estado]:
        return [self.to_entity_estado(model) for model in models]

    def to_entity_estado(self, model) -> Estado:
        return Estado(
            id_estado=model,
            nombre=model.nombre
        )

    def to_entity_municipio(self, model) -> Municipio:
        return Municipio(
            id_municipio=model.id,
            nombre=model.nombre,
            estado=self.to_entity_estado(model.estado)
        )

    def to_entity_colonia(self, model) -> Colonia:
        return Colonia(
            id_colonia=model.id,
            nombre=model.nombre,
            ciudad=model.ciudad,
            municipio=self.to_entity_municipio(model.municipio),
            asentamiento=model.asentamiento,
            codigo_postal=model.codigo_postal
        )
