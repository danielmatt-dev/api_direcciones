from dataclasses import dataclass
from api_direcciones.estado.core.entities.estado import Estado


@dataclass
class Municipio:
    id_municipio: int
    nombre: str
    estado: Estado
