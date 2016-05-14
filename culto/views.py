from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from .models import *
from django.utils import timezone


def dicc_calendar(year, month):
    mes = timezone.datetime(year, month + 1, 1) - timezone.timedelta(days=1)
    calendario = []
    dicc = {}
    primera_columna = True
    cultos = Cultos.objects.filter(fecha__year=year, fecha__month=month).order_by('fecha')
    eventos = Eventos.objects.filter(fecha__year=year, fecha__month=month).order_by('fecha')
    for x in xrange(1, mes.day + 1):
        dicc = {}
        dia = timezone.datetime(year, month, x)
        if primera_columna:
            if dia.weekday() > 0:
                for y in xrange(0, dia.weekday()):
                    dicc = {
                        "dia": ""
                    }
                    if y == 0:
                        dicc['Lunes'] = True
                    else:
                        dicc['Lunes'] = False
                    calendario.append(dicc)
            primera_columna = False
        dicc = {
            "dia": dia.day
        }
        for x in cultos:
            if x.fecha.day == dia.day:
                dicc['id_culto'] = x.id
                dicc['culto'] = True
        for x in eventos:
            if x.fecha.day == dia.day:
                dicc['id_evento'] = x.id
                dicc['evento'] = True
        if dia.weekday() == 0:
            dicc['Lunes'] = True
        else:
            dicc['Lunes'] = False
        calendario.append(dicc)
    return calendario


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
            for x in xrange(cultos[0].fecha.year, now.year):
                years.append(x)
        calendario = dicc_calendar(now.year, now.month)
        import ipdb; ipdb.set_trace()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))
