from abc import ABC, abstractmethod


class BuscarColonias(ABC):

    @abstractmethod
    def execute(self, codigo_postal):
        pass
