from django.db import models

from api_direcciones.estado.infraestructure.persistence.models.estado_model import EstadoModel


class MunicipioModel(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT, related_name="id_estado")
