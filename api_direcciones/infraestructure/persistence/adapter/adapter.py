from typing import List
from injector import inject

from api_direcciones.core.entities.entities import Colonia
from api_direcciones.core.port.repository import Repository
from api_direcciones.infraestructure.persistence.mapper.mapper import Mapper
from api_direcciones.infraestructure.persistence.models.models import ColoniaModel


class Adapter(Repository):

    @inject
    def __init__(self, mapper: Mapper):
        self.mapper = mapper

    def buscar_colonias_por_codigo_postal(self, codigo_postal: int) -> List[Colonia]:
        colonias = ColoniaModel.objects.filter(codigo_postal=codigo_postal)
        return self.mapper.to_list_entity_colonias(colonias)
