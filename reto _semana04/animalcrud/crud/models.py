from django.db import models

# Create your models here.
class AnimalModel(models.Model):
  animalId = models.AutoField(
    primary_key=True,
    unique=True,
    null=False,
    db_column='id'
  )
  animalEspecie = models.CharField(
    max_length = 25,
    null = False,
    db_column='especie',
  )
  animalNombre = models.CharField(
    max_length = 30,
    null = True,
    db_column='nombre',
  )
  animalEdad = models.IntegerField(
    db_column='edad',
    null=False,
  )
  class Meta:
    db_table='animales'