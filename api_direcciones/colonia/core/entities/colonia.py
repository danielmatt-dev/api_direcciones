from dataclasses import dataclass
from api_direcciones.municipio.core.entities.municipio import Municipio


@dataclass
class Colonia:
    id_colonia: int
    nombre: str
    ciudad: str
    municipio: Municipio
    asentamiento: str
    codigo_postal: int
