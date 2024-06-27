from django.db import models


class EstadoModel(models.Model):
    id_estado = models.AutoField(primary_key=True, db_column='id_estado')
    nombre = models.CharField(max_length=50, db_column='nombre')

    class Meta:
        db_table = 'estados'
        managed = False


class MunicipioModel(models.Model):
    id_municipio = models.AutoField(primary_key=True, db_column='id_municipio')
    nombre = models.CharField(max_length=50, db_column='nombre')
    estado = models.ForeignKey('EstadoModel',
                               on_delete=models.PROTECT,
                               db_column='id_estado',
                               related_name="municipios")

    class Meta:
        db_table = 'municipios'
        managed = False


class ColoniaModel(models.Model):
    id_colonia = models.AutoField(primary_key=True, db_column='id_colonia')
    nombre = models.CharField(max_length=100, db_column='nombre')
    ciudad = models.CharField(max_length=50, db_column='ciudad')
    municipio = models.ForeignKey('MunicipioModel',
                                  on_delete=models.PROTECT,
                                  db_column='id_municipio',
                                  related_name="colonias")
    asentamiento = models.CharField(max_length=25, db_column='asentamiento')
    codigo_postal = models.IntegerField(db_column='codigo_postal')

    class Meta:
        db_table = 'colonias'
        managed = False
    