from typing import List

from api_direcciones.core.entities.entities import Colonia
from api_direcciones.core.port.repository import Repository
from api_direcciones.infraestructure.persistence.models.models import ColoniaModel


class Adapter(Repository):

    def __init__(self, mapper_entities):
        self.mapper = mapper_entities

    def buscar_colonias_por_codigo_postal(self, codigo_postal) -> List[Colonia]:
        colonias = ColoniaModel.objects.filter(codigo_postal=codigo_postal)
        return self.mapper.to_list_entity_estados(colonias)
