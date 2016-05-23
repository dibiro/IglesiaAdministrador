from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
               url(r'^$', login_required(Cronograma.as_view()),
                   name='Culto'),
               url(r'^Direccion/$', login_required(Direccion.as_view()),
                   name='Direccion'),
               url(r'^DirigirCulto/(?P<pk>[0-9]+)/$',
                   login_required(DirigirCulto.as_view()),
                   name='DirigirCulto'),
               url(r'^Espectador/$', Espectador.as_view(),
                   name='Espectador'),
               url(r'^EspectarCulto/(?P<pk>[0-9]+)/$',
                   EspectarCulto.as_view(),
                   name='EspectarCulto'),
               url(r'^calendario/$',
                   login_required(dicc_calendar), name="calendario"),
               url(r'^crear_culto/$',
                   login_required(crear_culto), name="crear_culto"),
               url(r'^get_culto/$',
                   login_required(get_culto), name="get_culto"),
               url(r'^get_eventos/$',
                   login_required(get_eventos), name="get_eventos"),
               url(r'^buscar_versiculos_por_capitulo/$',
                   login_required(buscar_versiculos_por_capitulo),
                   name="buscar_versiculos_por_capitulo"),
               url(r'^buscar_versiculos_por_filtrado/$',
                   login_required(buscar_versiculos_por_filtrado),
                   name="buscar_versiculos_por_filtrado"),
               url(r'^mensaje/$',
                   login_required(mensaje), name="mensaje"),
               url(r'^nuevo_mensaje/$',
                   login_required(nuevo_mensaje), name="nuevo_mensaje"),
               url(r'^seleccionar_versiculo/$',
                   login_required(seleccionar_versiculo),
                   name="seleccionar_versiculo"),
               url(r'^espectador_de_culto/$',
                   espectador_de_culto, name="espectador_de_culto"),
               url(r'^invitar_culto/$',
                   login_required(invitar_culto), name="invitar_culto"),
              ]
