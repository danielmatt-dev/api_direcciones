# factories.py
from injector import Injector

from api_direcciones.core.use_cases.buscar_colonias import BuscarColonias
from api_direcciones.infraestructure.delivery.dto.mapper.mapper_dto import MapperDto
from api_direcciones.infraestructure.delivery.views.direccion_views import get_direcciones
from injector_modules import AppModule


def get_direcciones_factory(request, codigo_postal):
    injector = Injector([AppModule])
    buscar_colonias = injector.get(BuscarColonias)
    mapper_dto = injector.get(MapperDto)
    return get_direcciones(request, codigo_postal, buscar_colonias, mapper_dto)
