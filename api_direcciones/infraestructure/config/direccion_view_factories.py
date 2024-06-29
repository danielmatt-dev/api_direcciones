from injector import Injector

from api_direcciones.core.use_cases.buscar_colonias import BuscarColonias
from api_direcciones.core.use_cases.crear_usuario import CrearUsuario
from api_direcciones.core.use_cases.verificar_existencia_usuario import VerificarExistenciaUsuario
from api_direcciones.infraestructure.delivery.dto.mapper.mapper_dto import MapperDto
from api_direcciones.infraestructure.delivery.views.direccion_views import get_direcciones, post_crear_usuario
from injector_modules import AppModule


def get_direcciones_factory(request, codigo_postal):
    injector = Injector([AppModule])
    buscar_colonias = injector.get(BuscarColonias)
    mapper_dto = injector.get(MapperDto)
    return get_direcciones(request, codigo_postal, buscar_colonias, mapper_dto)


def post_crear_usuario_factory(request):
    injector = Injector([AppModule])
    verificar_existencia_usuario = injector.get(VerificarExistenciaUsuario)
    crear_usuario = injector.get(CrearUsuario)
    mapper_dto = injector.get(MapperDto)
    return post_crear_usuario(request, verificar_existencia_usuario, crear_usuario, mapper_dto)
