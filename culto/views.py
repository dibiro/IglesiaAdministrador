from django.shortcuts import render_to_response, HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from .models import *
from biblia.models import *
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
    cultos = Cultos.objects.filter(fecha__year=year,
                                   fecha__month=month).order_by('fecha')
    eventos = Eventos.objects.filter(fecha__year=year,
                                     fecha__month=month).order_by('fecha')
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
                    dicc['class'] = '"'
                    calendario.append(dicc)
            primera_columna = False
        dicc = {
            "dia": dia.day,
            "class": '"'
        }
        for x in cultos:
            if x.fecha.day == dia.day:
                dicc['class'] = 'success eventos" data-toggle="modal"'
                dicc['class'] += 'data-target="#visulizar"'
        for x in eventos:
            if x.fecha.day == dia.day:
                dicc['class'] = 'success eventos" data-toggle="modal"'
                dicc['class'] += ' data-target="#visulizar"'
        dicc['weekday'] = dia.weekday()
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
            for x in xrange(cultos[0].fecha.year, now.year + 1):
                years.append(x)
        else:
            years.append(now.year)
        hermanos = Hermanos.objects.all()
        tipos_de_cultos = TipoDeCulto.objects.all()
        return render_to_response(self.template_name, locals(),
                                  context_instance=RequestContext(request))


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
        escuela_dominical_id=request.POST['Escuela_dominical'],
        escuela_de_nino_id=request.POST['Escuela_De_ninos'],
    )
    culto.save()
    estado = EstadoDelCulto(culto=culto)
    estado.save()
    now = timezone.now()
    result = json.dumps({'year': now.year, 'month': now.month},
                        ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def get_culto(request):
    culto = Cultos.objects.get(id=request.GET['id'])
    dicc = {
        'id': culto.id,
        'Fecha': culto.fecha.strftime('%Y-%m-%d'),
        'Direccion': culto.Direccion.id,
        'Lectura': culto.lectura.id,
        'Recolecion': culto.recolecion.id,
        'Oracion': culto.oracion.id,
        'Coros': culto.coros.id,
        'Predicacion': culto.predicacion.id,
        'tipos_de_cultos': culto.tipo.id,
    }
    if culto.escuela_dominical is not None:
        dicc['escuela_dominical'] = culto.escuela_dominical.id,
    else:
        dicc['escuela_dominical'] = '',
    if culto.escuela_de_nino is not None:
        dicc['escuela_de_nino'] = culto.escuela_de_nino.id,
    else:
        dicc['escuela_de_nino'] = '',
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def get_eventos(request):
    cultos = Cultos.objects.filter(fecha__year=request.GET['year'],
                                   fecha__month=request.GET['mouth'],
                                   fecha__day=request.GET['day'])
    eventos = Eventos.objects.filter(fecha__year=request.GET['year'],
                                     fecha__month=request.GET['mouth'],
                                     fecha__day=request.GET['day'])
    dicc = {}
    lista = []
    for x in cultos:
        dicc = {
            "id": x.id,
            "direccion": x.Direccion.nombre + ' ' + x.Direccion.apellido,
            "nombre": x.tipo.nombre,
            "tipo": '1'
        }
        lista.append(dicc)
    for x in eventos:
        dicc = {
            "id": x.id,
            "nombre": x.nombre,
            "descripcion": x.descripcion,
            "hora": x.hora.strftime('%H-%M'),
            "encargado": x.encargado.nombre + ' ' + x.encargado.apellido,
            "tipo": '2'
        }
        lista.append(dicc)
    result = json.dumps(lista, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


class Direccion(TemplateView):
    template_name = "direccion_de_culto.html"

    def get(self, request, *args, **kwargs):
        now = timezone.now()
        cultos = Cultos.objects.filter(fecha__year=now.year,
                                       fecha__month=now.month,
                                       fecha__day=now.day,
                                       Direccion__user=request.user)
        eventos = Eventos.objects.filter(fecha__year=now.year,
                                         fecha__month=now.month,
                                         fecha__day=now.day,
                                         encargado__user=request.user)
        mensaje = 'Hoy No hay Cultos o Eventos donde seas Director'
        for x in cultos:
            mensaje = ''
        for x in eventos:
            mensaje = ''
        return render_to_response(self.template_name, locals(),
                                  context_instance=RequestContext(request))


class DirigirCulto(TemplateView):
    template_name = "DirigirCulto.html"

    def get(self, request, pk, *args, **kwargs):
        now = timezone.now()
        cultos = Cultos.objects.filter(id=pk, Direccion__user=request.user)
        mensaje = True
        for x in cultos:
            mensaje = False
        libros = Libros.objects.all()
        lista = []
        for x in xrange(1, 51):
            lista.append(x)
        genesis = Versiculos.objects.filter(libro=1,
                                            capitulo=1).order_by('versiculo')
        aux = 0
        lista_versiculos = []
        for x in genesis:
            lista_versiculos.append(x.versiculo)
            if x.versiculo > aux:
                aux = x.versiculo
        start_date = now + timezone.timedelta(days=1)
        end_date = now + timezone.timedelta(days=7)
        cultos_proximos = Cultos.objects.filter(
            fecha__range=(start_date.date(), end_date.date())
        )
        eventos_proximos = Eventos.objects.filter(
            fecha__range=(start_date.date(), end_date.date())
        )
        invitar = IvitacionDelCulto.objects.filter(culto=cultos)
        for x in invitar:
            dicc_select = {
                '1': True,
                '2': True,
                '3': True,
                '4': True,
                '5': True,
                '6': True,
                '7': True,
                '8': True,
            }
            if x.escuela_dominical:
                dicc_select['2'] = False
            elif x.escuela_de_nino:
                dicc_select['3'] = False
            elif x.Direccion:
                dicc_select['4'] = False
            elif x.lectura:
                dicc_select['5'] = False
            elif x.recolecion:
                dicc_select['6'] = False
            elif x.oracion:
                dicc_select['7'] = False
            elif x.coros:
                dicc_select['8'] = False
            elif x.predicacion:
                pass
            else:
                dicc_select['1'] = False
        return render_to_response(self.template_name, locals(),
                                  context_instance=RequestContext(request))


def buscar_versiculos_por_capitulo(request):
    numero_capitulos = 0
    capitulo = Versiculos.objects.filter(libro=request.GET['libro']
                                         ).order_by('capitulo')
    for x in capitulo:
        if x.capitulo > numero_capitulos:
            numero_capitulos = x.capitulo
    libro = Versiculos.objects.filter(libro=request.GET['libro'],
                                      capitulo=request.GET['capitulo']
                                      ).order_by('versiculo')
    aux = 0
    lista_versiculos = []
    dicc = {}
    for x in libro:
        if x.versiculo > aux:
            aux = x.versiculo
        dicc = {
            'id': x.id,
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
    libro = Versiculos.objects.filter(libro=request.GET['libro'],
                                      capitulo=request.GET['capitulo']
                                      ).order_by('versiculo')
    aux = 0
    lista_versiculos = []
    dicc = {}
    for x in libro:
        if x.versiculo > aux:
            aux = x.versiculo
        if x.versiculo >= int(request.GET['desde']) and x.versiculo <= int(request.GET['hasta']):
            dicc = {
                'id': x.id,
                'texto': x.texto,
                'versiculo': x.versiculo
            }
            lista_versiculos.append(dicc)
        dicc = {}
    estado = EstadoDelCulto.objects.get(culto=request.GET['id'])
    estado.versiculos = True
    estado.invitacion = False
    estado.anuncio = False
    estado.coros = False
    estado.save()
    if VersiculoDelCulto.objects.filter(culto=request.GET['id']).exists():
        versiculo = VersiculoDelCulto.objects.get(culto=request.GET['id'])
        versiculo.libro = Libros.objects.get(id=request.GET['libro'])
        versiculo.capitulo = request.GET['capitulo']
        versiculo.desde = request.GET['desde']
        versiculo.hasta = request.GET['hasta']
        versiculo.todos = True
        versiculo.fecha_modificado = timezone.now()
        versiculo.save()
    else:
        versiculo = VersiculoDelCulto(
            culto_id=request.GET['id'],
            libro_id=request.GET['libro'],
            capitulo=request.GET['capitulo'],
            desde=request.GET['desde'],
            hasta=request.GET['hasta'],
            todos=True,
            fecha_modificado=timezone.now()
        )
        versiculo.save()
    result = json.dumps(lista_versiculos, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


class Espectador(TemplateView):
    template_name = "espectador_de_culto.html"

    def get(self, request, *args, **kwargs):
        now = timezone.now()
        cultos = Cultos.objects.filter(fecha__year=now.year,
                                       fecha__month=now.month,
                                       fecha__day=now.day)
        eventos = Eventos.objects.filter(fecha__year=now.year,
                                         fecha__month=now.month,
                                         fecha__day=now.day)
        mensaje = 'Hoy No hay Cultos'
        for x in cultos:
            mensaje = ''
        for x in eventos:
            mensaje = ''
        return render_to_response(self.template_name, locals(),
                                  context_instance=RequestContext(request))


class EspectarCulto(TemplateView):
    template_name = "EspectarCulto.html"

    def get(self, request, pk, *args, **kwargs):
        cultos = Cultos.objects.filter(id=pk)
        return render_to_response(self.template_name, locals(),
                                  context_instance=RequestContext(request))


def mensaje(request):
    comentarios = Comentarios.objects.filter(id__gte=request.GET['id'],
                                             culto=request.GET['culto']
                                             ).order_by('id')
    dicc = {}
    lista = []
    for x in comentarios:
        dicc = {
            "id": x.id,
            'comentarios': x.comentario,
            'fecha': x.fecha.strftime('%Y-%m-%d %H:%M:%S'),
        }
        if x.hermano.user.id == request.user.id:
            dicc['user'] = 1
        else:
            dicc['user'] = x.hermano.nombre + ' ' + x.hermano.apellido
        lista.append(dicc)
        dicc = {}
    result = json.dumps(lista, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def nuevo_mensaje(request):
    comentario = Comentarios(
        comentario=request.POST['comentario'],
        hermano=Hermanos.objects.get(user=request.user),
        culto_id=request.POST['culto'],
    )
    comentario.save()
    result = json.dumps("listo", ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def seleccionar_versiculo(request):
    versiculo = VersiculoDelCulto.objects.filter(culto=request.GET['id_culto']).update(
        selecionado_id=request.GET['id'],
        todos=False,
        fecha_modificado=timezone.now()
    )
    result = json.dumps("listo", ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def espectador_de_culto(request):
    culto = EstadoDelCulto.objects.get(culto=request.GET['culto'])
    dicc = {'tipo': 0}
    dicc2 = {}
    lista = []
    if culto.versiculos:
        versiculo = VersiculoDelCulto.objects.get(culto=culto.culto)
        dicc = {
            'tipo': 1,
            'libro': versiculo.libro.nombre,
            'capitulo': versiculo.capitulo,
            'desde': versiculo.desde,
            'hasta': versiculo.hasta,
            'fecha': versiculo.fecha_modificado.strftime('%Y-%m-%d %H:%M:%S'),
        }
        if versiculo.todos:
            versiculos = Versiculos.objects.filter(libro=versiculo.libro,
                                                   capitulo=versiculo.capitulo)
            for x in versiculos:
                if x.versiculo >= versiculo.desde and x.versiculo <= versiculo.hasta:
                    dicc2 = {
                        'id': x.id,
                        'texto': x.texto,
                        'versiculo': x.versiculo
                    }
                    lista.append(dicc2)
            dicc['selecionados'] = lista
        else:
            dicc['selecionados'] = [
                {
                    'id': versiculo.selecionado.id,
                    'texto': versiculo.selecionado.texto,
                    'versiculo': versiculo.selecionado.versiculo
                }
            ]
    elif culto.invitacion:
        pass
    elif culto.anuncio:
        pass
    elif culto.coros:
        pass
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def invitar_culto(request):
    target = request.GET['target']
    estado = EstadoDelCulto.objects.get(culto=request.GET['id_culto'])
    estado.versiculos = False
    estado.invitacion = True
    estado.anuncio = False
    estado.coros = False
    estado.save()
    estado = IvitacionDelCulto.objects.get(culto=request.GET['id_culto'])
    estado.escuela_de_nino = False
    estado.escuela_dominical = False
    estado.Direccion = False
    estado.lectura = False
    estado.recolecion = False
    estado.oracion = False
    estado.coros = False
    estado.predicacion = False
    if request.GET['target'] == '1':
        estado.escuela_de_nino = True
    elif request.GET['target'] == '2':
        estado.escuela_dominical = True
    elif request.GET['target'] == '3':
        estado.Direccion = True
    elif request.GET['target'] == '4':
        estado.lectura = True
    elif request.GET['target'] == '5':
        estado.recolecion = True
    elif request.GET['target'] == '6':
        estado.oracion = True
    elif request.GET['target'] == '7':
        estado.coros = True
    elif request.GET['target'] == '8':
        estado.predicacion = True
    estado.save()
    result = json.dumps(target, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')
