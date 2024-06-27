from dataclasses import dataclass
from typing import List


@dataclass
class Direccion:
    codigo_postal: str
    colonias: List[str]
    estado: str
    ciudad: str
    asentamiento: str
    pais = str

    def to_json(self):
        return {
            'codigo_postal': self.codigo_postal,
            'colonias': self.colonias,
            'estado': self.estado,
            'ciudad': self.ciudad,
            'asentamiento': self.asentamiento,
            'pais': self.pais
        }
