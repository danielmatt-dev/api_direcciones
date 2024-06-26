from django.db import models

from api_direcciones.municipio.infraestructure.persistence.models.municipio_model import MunicipioModel


class ColoniaModel(models.Model):
    nombre = models.CharField(max_length=50)
    municipio = models.ForeignKey(MunicipioModel, on_delete=models.PROTECT, related_name="id_municipio")
