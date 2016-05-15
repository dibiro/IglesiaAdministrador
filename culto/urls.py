from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = patterns('',
                       url(r'^$', login_required(Cronograma.as_view()),
                       	   name='Culto'),
                       url(r'^calendario/$',
                       	   login_required(dicc_calendar), name="calendario"),
                       url(r'^crear_culto/$',
                       	   login_required(crear_culto), name="crear_culto"),
                       url(r'^get_culto/$',
                       	   login_required(get_culto), name="get_culto"),
                       )
