from injector import inject

from api_direcciones.core.port.repository import Repository
from api_direcciones.core.use_cases.buscar_colonias import BuscarColonias


class BuscarColoniasImpl(BuscarColonias):

    @inject
    def __init__(self, repository: Repository):
        self.repository = repository

    def execute(self, codigo_postal):
        return self.repository.buscar_colonias_por_codigo_postal(codigo_postal)
