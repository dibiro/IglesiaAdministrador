from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Libros(models.Model):
    TESTAMENTO_OPCION = (("1", "Antiguo"), ("2", "Nuevo"))
    nombre = models.CharField(max_length=50)
    testamento = models.CharField(max_length=2, choices=TESTAMENTO_OPCION, blank=True, null=True)
    capitulos = models.PositiveIntegerField(blank=True, null=True)
    
    def get_testamento(self):
        if self.testamento == '1':
            return u"Antiguo"
        elif self.testamento == '2':
            return u"Nuevo"

    class Meta:
        db_table = 'libros'

    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.testamento)


class Versiculos(models.Model):
    libro = models.ForeignKey(Libros)
    bibla = models.PositiveIntegerField()
    capitulo = models.PositiveIntegerField()
    versiculo = models.PositiveIntegerField()
    texto = models.CharField(max_length=500)

    class Meta:
        db_table = 'versiculos'

    def __unicode__(self):
        return '%s %s:%s, %s' % (self.libro, self.capitulo, self.versiculo, self.texto)

