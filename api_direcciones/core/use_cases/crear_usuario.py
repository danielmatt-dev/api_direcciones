from abc import ABC, abstractmethod

from rest_framework_simplejwt.tokens import Token


class CrearUsuario(ABC):

    @abstractmethod
    def execute(self, usuario) -> Token:
        pass
