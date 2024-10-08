from typing import List
from django.contrib.auth.models import User
from injector import inject
from rest_framework_simplejwt.tokens import RefreshToken, Token

from api_direcciones.core.entities.entities import Colonia
from api_direcciones.core.port.repository import Repository
from api_direcciones.infraestructure.persistence.mapper.mapper import Mapper
from api_direcciones.infraestructure.persistence.models.models import ColoniaModel


class Adapter(Repository):

    @inject
    def __init__(self, mapper: Mapper):
        self._mapper = mapper

    def buscar_colonias_por_codigo_postal(self, codigo_postal: int) -> List[Colonia]:
        colonias = ColoniaModel.objects.filter(codigo_postal=codigo_postal)
        return self._mapper.to_list_entity_colonias(colonias)

    def verificar_existencia_usuario(self, username) -> bool:
        return User.objects.filter(username=username).exists()

    def crear_usuario(self, usuario) -> Token:
        user = User.objects.create_user(
            username=usuario.username,
            password=usuario.password,
            email=usuario.email
        )

        return RefreshToken.for_user(user)
