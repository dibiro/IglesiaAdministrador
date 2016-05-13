from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name='Hermanos'),
                       )
