from dataclasses import dataclass


@dataclass
class Estado:
    id_estado: int
    nombre: str
    pais: str = 'México'


@dataclass
class Municipio:
    id_municipio: int
    nombre: str
    estado: Estado


@dataclass
class Colonia:
    id_colonia: int
    nombre: str
    ciudad: str
    municipio: Municipio
    asentamiento: str
    codigo_postal: int
