from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import *


admin.site.register(Libros)
admin.site.register(Versiculos)
