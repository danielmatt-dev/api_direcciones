from abc import ABC, abstractmethod


class VerificarExistenciaUsuario(ABC):

    @abstractmethod
    def execute(self, username) -> bool:
        pass
