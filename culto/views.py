from django.shortcuts import render_to_response, HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from .models import *
from hermanos.models import *
from django.utils import timezone
import json


def dicc_calendar(request):
    year = int(request.GET['year'])
    month = int(request.GET['mouth'])
    mes = timezone.datetime(year, month + 1, 1) - timezone.timedelta(days=1)
    calendario = []
    dicc = {}
    primera_columna = True
    cultos = Cultos.objects.filter(fecha__year=year, fecha__month=month).order_by('fecha')
    eventos = Eventos.objects.filter(fecha__year=year, fecha__month=month).order_by('fecha')
    if_culto = Cultos.objects.filter(fecha__year=year, fecha__month=month).exists()
    if_evento = Eventos.objects.filter(fecha__year=year, fecha__month=month).exists()
    for x in xrange(1, mes.day + 1):
        dicc = {}
        dia = timezone.datetime(year, month, x)
        if primera_columna:
            if dia.weekday() > 0:
                for y in xrange(0, dia.weekday()):
                    dicc = {
                        "dia": ""
                    }
                    dicc['weekday'] = y
                    dicc['culto'] = 0
                    dicc['evento'] = 0
                    calendario.append(dicc)
            primera_columna = False
        dicc = {
            "dia": dia.day
        }
        for x in cultos:
            if x.fecha.day == dia.day:
                dicc['id_culto'] = x.id
                dicc['culto'] = 1
            else:
                dicc['culto'] = 0
        for x in eventos:
            if x.fecha.day == dia.day:
                dicc['id_evento'] = x.id
                dicc['evento'] = 1
            else:
                dicc['evento'] = 0
        dicc['weekday'] = dia.weekday()
        if not if_culto:
            dicc['culto'] = 0
        if not if_evento:
            dicc['evento'] = 0
        calendario.append(dicc)
    result = json.dumps(calendario, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


class Cronograma(TemplateView):
    template_name = "Cronograma.html"

    def get(self, request, *args, **kwargs):
        now = timezone.now()
        meses = []
        years = []
        cultos = Cultos.objects.all().order_by('fecha')
        for x in xrange(1, 12):
            meses.append(x)
        if Cultos.objects.all().exists():
            for x in xrange(cultos[0].fecha.year, now.year+1):
                years.append(x)
        else:
            years.append(now.year)
        hermanos = Hermanos.objects.all()
        tipos_de_cultos = TipoDeCulto.objects.all()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


def crear_culto(request):
    culto = Cultos(
        fecha=request.POST['fecha'],
        Direccion_id=request.POST['Direccion'],
        lectura_id=request.POST['lectura'],
        recolecion_id=request.POST['recolecion'],
        oracion_id=request.POST['oracion'],
        coros_id=request.POST['coros'],
        predicacion_id=request.POST['predicacion'],
        tipo_id=request.POST['tipo'],
    )
    culto.save()
    now = timezone.now()
    result = json.dumps({'year': now.year, 'month': now.month}, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')
