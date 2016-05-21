from __future__ import unicode_literals
from django.db import models
from hermanos.models import Hermanos
from biblia.models import Libros, Versiculos


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


class Comentarios(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    hermano = models.ForeignKey(Hermanos)
    comentario = models.TextField()
    culto = models.ForeignKey(Cultos)

    class Meta:
        db_table = 'comentarios'

    def __unicode__(self):
        return '%s - %s - %s' % (self.fecha, self.culto, self.hermano)


class EstadoDelCulto(models.Model):
    culto = models.OneToOneField(Cultos)
    versiculos = models.BooleanField(default=False)
    invitacion = models.BooleanField(default=False)
    anuncio = models.BooleanField(default=False)
    coros = models.BooleanField(default=False)

    class Meta:
        db_table = 'estado_del_culto'

    def __unicode__(self):
        return '%s' % self.culto


class VersiculoDelCulto(models.Model):
    culto = models.OneToOneField(Cultos)
    libro = models.ForeignKey(Libros)
    capitulo = models.PositiveIntegerField()
    desde = models.PositiveIntegerField()
    hasta = models.PositiveIntegerField()
    selecionado = models.ForeignKey(Versiculos, blank=True, null=True)
    todos = models.BooleanField()
    fecha_modificado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'versiculo_del_culto'

    def __unicode__(self):
        return '%s - %s' % (self.culto, self.selecionado)


class IvitacionDelCulto(models.Model):
    culto = models.OneToOneField(Cultos)
    Direccion = models.BooleanField(default=False)
    lectura = models.BooleanField(default=False)
    recolecion = models.BooleanField(default=False)
    oracion = models.BooleanField(default=False)
    coros = models.BooleanField(default=False)
    predicacion = models.BooleanField(default=False)
    fecha_modificado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'invitacion_del_culto'

    def __unicode__(self):
        return '%s' % self.culto
