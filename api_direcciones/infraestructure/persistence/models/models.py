from django.db import models


class EstadoModel(models.Model):
    nombre = models.CharField(max_length=50)


class MunicipioModel(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(EstadoModel, on_delete=models.PROTECT, related_name="id_estado")


class ColoniaModel(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    municipio = models.ForeignKey(MunicipioModel, on_delete=models.PROTECT, related_name="id_municipio")
    asentamiento = models.CharField(max_length=25)
    codigo_postal = models.IntegerField(max_length=5)
    