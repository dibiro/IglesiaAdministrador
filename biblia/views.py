# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response, HttpResponse, render
from django.template import RequestContext
from .models import * 
import json
from django.conf import settings as _settings
from django.contrib.auth import login, logout, authenticate
from django.core.mail import get_connection, send_mail, BadHeaderError


class BuscarVersiculo(TemplateView):
    template_name = "BuscarVersiculo.html"

    def get(self, request, *args, **kwargs):
        libros = Libros.objects.all()
        lista = []
        for x in xrange(1,51):
            lista.append(x)
        genesis = Versiculos.objects.filter(libro=1, capitulo=1).order_by('versiculo')
        aux = 0
        lista_versiculos = []
        for x in genesis:
            lista_versiculos.append(x.versiculo)
            if x.versiculo > aux:
                aux = x.versiculo
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


def buscar_versiculos_por_capitulo(request):
    numero_capitulos = 0
    capitulo = Versiculos.objects.filter(libro=request.GET['libro']).order_by('capitulo')
    for x in capitulo:
        if x.capitulo > numero_capitulos:
            numero_capitulos = x.capitulo
    libro = Versiculos.objects.filter(libro=request.GET['libro'], capitulo=request.GET['capitulo']).order_by('versiculo')
    aux = 0
    lista_versiculos = []
    dicc = {}
    for x in libro:
        if x.versiculo > aux:
            aux = x.versiculo
        dicc = {
            'texto': x.texto,
            'versiculo': x.versiculo
        }
        lista_versiculos.append(dicc)
        dicc = {}
    dicc = {
        'versiculos': lista_versiculos,
        'numero_versiculos': aux,
        'numero_capitulos': numero_capitulos
    }
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def buscar_versiculos_por_filtrado(request):
    libro = Versiculos.objects.filter(libro=request.GET['libro'], capitulo=request.GET['capitulo']).order_by('versiculo')
    aux = 0
    lista_versiculos = []
    dicc = {}
    for x in libro:
        if x.versiculo > aux:
            aux = x.versiculo
        if x.versiculo >= int(request.GET['desde']) and x.versiculo <= int(request.GET['hasta']):
            dicc = {
                'texto': x.texto,
                'versiculo': x.versiculo
            }
            lista_versiculos.append(dicc)
        dicc = {}
    result = json.dumps(lista_versiculos, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')