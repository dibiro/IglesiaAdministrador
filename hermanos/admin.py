from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import *


admin.site.register(LogEntry)
admin.site.register(Hermanos)
admin.site.register(Ministerios)
admin.site.register(Direccion)
admin.site.register(Telefono)
admin.site.register(Bitacora)
