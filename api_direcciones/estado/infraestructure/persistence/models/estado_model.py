from django.db import models


class EstadoModel(models.Model):
    nombre = models.CharField(max_length=50)
