from injector import inject

from api_direcciones.core.port.repository import Repository
from api_direcciones.core.use_cases.verificar_existencia_usuario import VerificarExistenciaUsuario


class VerificarExistenciaUsuarioImpl(VerificarExistenciaUsuario):

    @inject
    def __init__(self, repository: Repository):
        self._repository = repository

    def execute(self, username) -> bool:
        return self._repository.verificar_existencia_usuario(username)
