from __future__ import unicode_literals
from django.db import models
from hermanos.models import Hermanos


class TipoDeCulto(models.Model):
    nombre = models.CharField(max_length=500)

    class Meta:
        db_table = 'tipos_de_cultos'

    def __unicode__(self):
        return '%s' % self.nombre


class Cultos(models.Model):
    fecha = models.DateField()
    Direccion = models.ForeignKey(Hermanos, related_name="Direccion")
    lectura = models.ForeignKey(Hermanos, related_name="lectura")
    recolecion = models.ForeignKey(Hermanos, related_name="recolecion")
    oracion = models.ForeignKey(Hermanos, related_name="oracion")
    coros = models.ForeignKey(Hermanos, related_name="coros")
    predicacion = models.ForeignKey(Hermanos, related_name="predicacion")
    tipo = models.ForeignKey(TipoDeCulto)

    class Meta:
        db_table = 'cultos'

    def __unicode__(self):
        return '%s - %s' % (self.fecha, self.tipo)


class Eventos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    descripcion = models.TextField()
    hora = models.TimeField()
    encargado = models.ForeignKey(Hermanos)

    class Meta:
        db_table = 'eventos'

    def __unicode__(self):
        return '%s' % self.nombre

