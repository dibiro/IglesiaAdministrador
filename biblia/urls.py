from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
               url(r'^$', BuscarVersiculo.as_view(), name='Biblia'),
               url(r'^buscar_versiculos_por_capitulo/$', buscar_versiculos_por_capitulo, name='buscar_versiculos_por_capitulo'),
               url(r'^buscar_versiculos_por_filtrado/$', buscar_versiculos_por_filtrado, name='buscar_versiculos_por_filtrado'),
               url(r'^calcular_capitulos/$', calcular_capitulos, name='calcular_capitulos'),
]
