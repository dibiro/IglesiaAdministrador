from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Bitacora(models.Model):
    TYPE_CHOICES = (("1", "Clientes"), ("2", "Pc"), ("3", "Telefono"), ("4", "Peticiones"), ("5", "Peticiones Completadas"), ("6", "Peticiones Entregadas"), ("7", "Usuarios"))
    ACTION_CHOICES = (("1", "Crear"), ("2", "Modificar"), ("3", "Elimina"))
    tipo = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True)
    object_id = models.BigIntegerField()
    accion = models.CharField(max_length=2, choices=ACTION_CHOICES, blank=True, null=True)
    descripcion = models.TextField()
    user = models.ForeignKey(User)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'bitacora'

    def get_action(self):
        if self.accion == '1':
            return mark_safe("<i class='fa fa-plus' data-toggle='tooltip' data-placement='top' title='Crear'></i>")
        elif self.accion == '2':
            return mark_safe("<i class='fa fa-pencil-square-o' data-toggle='tooltip' data-placement='top' title='Modificar'></i>")
        elif self.accion == '3':
            return mark_safe("<i class='fa fa-minus-square' data-toggle='tooltip' data-placement='top' title='Eliminar' style='color:red'></i>")
    get_action.allow_tags = True

    def get_type(self):
        if self.tipo == '1':
            return mark_safe("<i class='fa fa-users' data-toggle='tooltip' data-placement='top' title='Cliente'></i>")
        elif self.tipo == '2':
            return mark_safe("<i class='fa fa-laptop' data-toggle='tooltip' data-placement='top' title='Pc'></i>")
        elif self.tipo == '3':
            return mark_safe("<i class='fa fa-mobile' data-toggle='tooltip' data-placement='top' title='Telefonos'></i>")
        elif self.tipo == '4':
            return mark_safe("<i class='fa fa-puzzle-piece' data-toggle='tooltip' data-placement='top' title='Peticiones'></i>")
        elif self.tipo == '5':
            return mark_safe("<i class='fa fa-check' data-toggle='tooltip' data-placement='top' title='Peticiones Completadas'></i>")
        elif self.tipo == '6':
            return mark_safe("<i class='fa fa-check-circle' data-toggle='tooltip' data-placement='top' title='Peticiones Entregadas'></i>")
        elif self.tipo == '7':
            return mark_safe("<i class='fa fa-user' data-toggle='tooltip' data-placement='top' title='Usuarios'></i>")
    get_type.allow_tags = True

    def __unicode__(self):
        return '%s - %s' % (self.tipo, self.accion)


class Ministerios(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'ministerios'

    def __unicode__(self):
        return '%s' % self.nombre


class Hermanos(models.Model):
    SEX_CHOICES = (("1", "Masculino"), ("2", "Femenino"))
    cedula = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    ministerio = models.ForeignKey(Ministerios,  blank=True, null=True)
    user = models.OneToOneField(User)

    def get_sex(self):
        if self.sexo == '1':
            return u"Masculino"
        elif self.sexo == '2':
            return u"Femenino"

    class Meta:
        db_table = 'hermanos'

    def __unicode__(self):
        return '%s (%s %s)' % (self.cedula, self.nombre, self.apellido)


class Direccion(models.Model):
    hermano = models.ForeignKey(Hermanos)
    direccion = models.TextField()
    
    class Meta:
        db_table = 'direccion'

    def __unicode__(self):
        return '%s - %s' % (self.hermano, self.direccion)


class Telefono(models.Model):
    hermano = models.ForeignKey(Hermanos)
    telefono = models.CharField(max_length=50)

    class Meta:
        db_table = 'telefono'

    def __unicode__(self):
        return '%s - %s' % (self.hermano, self.telefono)

