from injector import Module, singleton, provider

from api_direcciones.core.port.repository import Repository
from api_direcciones.core.use_cases.buscar_colonias import BuscarColonias
from api_direcciones.core.use_cases.crear_usuario import CrearUsuario
from api_direcciones.core.use_cases.impl.buscar_colonias_impl import BuscarColoniasImpl
from api_direcciones.core.use_cases.impl.crear_usuario_impl import CrearUsuarioImpl
from api_direcciones.core.use_cases.impl.verificar_existencia_usuario_impl import VerificarExistenciaUsuarioImpl
from api_direcciones.core.use_cases.verificar_existencia_usuario import VerificarExistenciaUsuario
from api_direcciones.infraestructure.delivery.dto.mapper.mapper_dto import MapperDto, MapperDtoImpl
from api_direcciones.infraestructure.persistence.adapter.adapter import Adapter
from api_direcciones.infraestructure.persistence.mapper.mapper import Mapper
from api_direcciones.infraestructure.persistence.mapper.mapper_impl import MapperImpl


# >
class AppModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> Mapper:
        return MapperImpl()

    @singleton
    @provider
    def provide_repository(self) -> Repository:
        return Adapter(self.provide_mapper())

    @singleton
    @provider
    def provider_buscar_colonias(self) -> BuscarColonias:
        return BuscarColoniasImpl(self.provide_repository())

    @singleton
    @provider
    def provider_verificar_usuario(self) -> VerificarExistenciaUsuario:
        return VerificarExistenciaUsuarioImpl(self.provide_repository())

    @singleton
    @provider
    def provider_crear_usuario(self) -> CrearUsuario:
        return CrearUsuarioImpl(self.provide_repository())

    @singleton
    @provider
    def provider_mapper_dto(self) -> MapperDto:
        return MapperDtoImpl()
