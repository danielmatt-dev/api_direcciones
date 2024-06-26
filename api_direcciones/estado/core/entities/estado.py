from dataclasses import dataclass


@dataclass
class Estado:
    id_estado: int
    nombre: str
    pais: str = 'México'
