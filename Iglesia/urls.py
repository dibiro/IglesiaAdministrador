from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from biblia.views import *


urlpatterns = [
               url(r'^admin/', include(admin.site.urls)),
               url(r'^biblia/', BuscarVersiculo.as_view(), name='BuscarVersiculo'),
               url(r'^buscar_versiculos_por_capitulo/', buscar_versiculos_por_capitulo, name='buscar_versiculos_por_capitulo'),
               url(r'^buscar_versiculos_por_filtrado/', buscar_versiculos_por_filtrado, name='buscar_versiculos_por_filtrado'),
]
