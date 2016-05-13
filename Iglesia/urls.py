from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^Administrador/', include(admin.site.urls)),
                       url('^Biblia/', include('biblia.urls')),
                       url('^Hermanos/', include('hermanos.urls')),
                       )
