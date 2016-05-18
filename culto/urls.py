from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
               url(r'^$', login_required(Cronograma.as_view()),
                   name='Culto'),
               url(r'^Direccion/$', login_required(Direccion.as_view()),
                   name='Direccion'),
               url(r'^DirigirCulto/(?P<pk>[0-9]+)/$', login_required(DirigirCulto.as_view()),
                   name='DirigirCulto'),
               url(r'^calendario/$',
               	   login_required(dicc_calendar), name="calendario"),
               url(r'^crear_culto/$',
               	   login_required(crear_culto), name="crear_culto"),
               url(r'^get_culto/$',
               	   login_required(get_culto), name="get_culto"),
               url(r'^get_eventos/$',
               	   login_required(get_eventos), name="get_eventos"),
              ]
