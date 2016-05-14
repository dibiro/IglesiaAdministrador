from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^Administrador/', include(admin.site.urls)),
                       url('^Biblia/', include('biblia.urls')),
                       url('^Hermanos/', include('hermanos.urls')),
                       url('^Culto/', include('culto.urls')),
                       )
