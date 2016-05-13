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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class Index(TemplateView):
    template_name = "hermanos.html"

    def get(self, request, *args, **kwargs):
        hermanos = Hermanos.objects.all()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


def crear_hermano(request):
    hermano = Hermanos(
        cedula=request.POST['cedula'],
        nombre=request.POST['nombre'],
        sexo=request.POST['sexo'],
        apellido=request.POST['apellido'],
        fecha_de_nacimiento=request.POST['fecha_de_nacimiento'],
    )
    hermano.save()
    bitacora = Bitacora(
        tipo='1',
        object_id=hermano.id,
        accion='1',
        user=request.user,
    )
    descripcion='Se Registra al hermano Cedula: ' + hermano.cedula + ', ' + hermano.nombre + ' ' + hermano.apellido + ', sexo: ' + hermano.get_sex() + ', Fecha de nacimiento: ' + hermano.fecha_de_nacimiento
    telefonos = request.POST.getlist('telefonos[]')
    direcciones = request.POST.getlist('direcciones[]')
    aux = 1 
    for x in telefonos:
        if x != '':
            telefono = Telefono(
                hermano=hermano,
                telefono=x,
            )
            telefono.save()
            if aux == 1:
                descripcion += ' telefono(s): ' + x + ', '
            else:
                descripcion += x + ', ' 
            aux += 1
    aux = 1 
    for x in direcciones:
        if x != '':
            direccion = Direccion(
                hermano=hermano,
                direccion=x,
            )
            direccion.save()
            if aux == 1:
                descripcion += ' direccion(es): ' + x + ', '
            else:
                descripcion += x + ', '
            aux += 1
    bitacora.descripcion = descripcion
    bitacora.save()
    Hermanos = Hermanos.objects.all()
    lista = []
    dicc = {}
    for x in Hermanos:
        dicc = {
            'id': x.id,
            'nombre': x.cedula + ' - ' + x.nombre + ' ' + x.apellido,
        }
        lista.append(dicc)
        dicc = {}
    dicc = {
        'Hermanos': lista,
        'nuevo': hermano.id,
    }
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def update_hermano(request):
    if request.GET:
        dicc = {}
        lista_telefonos = []
        lista_direcciones = []
        hermano = Hermanos.objects.get(id=request.GET['id'])
        telefonos = Telefono.objects.filter(hermano=hermano)
        direcciones = Direccion.objects.filter(hermano=hermano)
        for x in telefonos:
            lista_telefonos.append(x.telefono)
        for x in direcciones:
            lista_direcciones.append(x.direccion)
        dicc = {
            'id': hermano.id,
            'cedula': hermano.cedula,
            'nombre': hermano.nombre,
            'apellido': hermano.apellido,
            'sexo': hermano.sexo,
            'fecha_de_nacimiento': hermano.fecha_de_nacimiento.strftime('%Y-%m-%d'),
            'telefonos': lista_telefonos,
            'direcciones': lista_direcciones,
        }
        result = json.dumps(dicc, ensure_ascii=False)
    if request.POST:
        cli = Hermanos.objects.get(id=request.POST['id'])
        hermano = Hermanos.objects.filter(id=request.POST['id']).update(
            cedula=request.POST["cedula"],
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            sexo=request.POST["sexo"],
            fecha_de_nacimiento=request.POST["fecha_de_nacimiento"],
        )
        hermano = Hermanos.objects.get(id=request.POST['id'])
        descripcion = ''
        if cli.cedula != request.POST["cedula"]:
            descripcion += "se modifca cedula: " + cli.cedula + ' por: ' + hermano.cedula + ', '
        if cli.nombre != request.POST["nombre"]:
            descripcion += "se modifca nombre: " + cli.nombre + ' por: ' + hermano.nombre + ', '
        if cli.apellido != request.POST["apellido"]:
            descripcion += "se modifca apellido: " + cli.apellido + ' por: ' + hermano.apellido + ', '
        if cli.sexo != request.POST["sexo"]:
            descripcion += "se modifca sexo: " + cli.sexo + ' por: ' + hermano.sexo + ', '
        if cli.fecha_de_nacimiento != request.POST["fecha_de_nacimiento"]:
            descripcion += "se modifca fecha de nacimiento: " + cli.fecha_de_nacimiento.strftime('%Y-%m-%d') + ' por: ' + hermano.fecha_de_nacimiento.strftime('%Y-%m-%d') + ', '
        telefono = Telefono.objects.filter(hermano=request.POST['id'])
        telefono.delete()
        direcciones = Direccion.objects.filter(hermano=request.POST['id'])
        direcciones.delete()
        telefonos = request.POST.getlist('telefonos[]')
        direcciones = request.POST.getlist('direcciones[]')
        aux = 1 
        for x in telefonos:
            if x != '':
                telefono = Telefono(
                    hermano=hermano,
                    telefono=x,
                )
                telefono.save()
                if aux == 1:
                    descripcion += ' telefono(s): ' + x + ', '
                else:
                    descripcion += x + ', ' 
                aux += 1
        aux = 1 
        for x in direcciones:
            if x != '':
                direccion = Direccion(
                    hermano=hermano,
                    direccion=x,
                )
                direccion.save()
                if aux == 1:
                    descripcion += ' direccion(es): ' + x + ', '
                else:
                    descripcion += x + ', '
                aux += 1
        if descripcion != '':
            bitacora = Bitacora(
                tipo='1',
                object_id=hermano.id,
                accion='2',
                user=request.user,
                descripcion=descripcion
            )
            bitacora.save()
        result = json.dumps("Actualizado", ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def change_password(request):
    if request.method == "POST":
        user = User.objects.get(id=request.POST["id"])
        user.set_password(request.POST["password"])
        user.save()
        if request.user.id != request.POST['id']:
            descripcion = 'El usuario ' + request.user.username + ' le modifico la clave al usuario ' + user.username
        else:
            descripcion = 'El usuario ' + user.username + ' cambio su clave'
        if descripcion != '':
            bitacora = Bitacora(
                tipo='7',
                object_id=user.id,
                accion='2',
                user_id=request.user.id,
                descripcion=descripcion
            )
            bitacora.save()
    return HttpResponse(json.dumps({"message": "password cambiada."}, ensure_ascii=False), content_type='application/json; charset=utf-8')


def update_user(request):
    if request.method == "GET":
        user = User.objects.get(id=request.GET["id"])
        dicc = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "admistrador": user.is_staff,
        }
    if request.method == "POST":
        user_old = User.objects.get(id=request.POST["id"])
        user = User.objects.get(id=request.POST["id"])
        user.username = request.POST["username"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        tipo = ''
        if request.POST.has_key('tipo'):
            if request.POST['tipo'] == '2':
                user.is_staff = True
                tipo = 'Administrador'
            elif request.POST['tipo'] == '1':
                user.is_staff = False
                tipo = 'Normal'
        user.save()
        dicc = {
            "id": request.POST["id"],
            "username": request.POST["username"],
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"] ,
        }
        descripcion = ''
        if user_old.username != user.username:
            descripcion += 'Se cambia username: ' + user_old.username + ' por: ' + user.username + ', '
        if user_old.first_name != user.first_name:
            descripcion += 'Se cambia nombre: ' + user_old.first_name + ' por: ' + user.first_name + ', '
        if user_old.last_name != user.last_name:
            descripcion += 'Se cambia apellido: ' + user_old.last_name + ' por: ' + user.last_name + ', '
        if user_old.email != user.email:
            descripcion += 'Se cambia email: ' + user_old.email + ' por: ' + user.email + ', '
        if user_old.is_staff != user.is_staff:
            descripcion += 'Ahora es un usuario de tipo ' + tipo
        if descripcion != '':  
            bitacora = Bitacora(
                tipo='7',
                object_id=user.id,
                accion='2',
                user=request.user,
                descripcion=descripcion
            )
            bitacora.save()
    return HttpResponse(json.dumps(dicc, ensure_ascii=False), content_type='application/json; charset=utf-8')


def revisar_cedula(request):
    if Hermanos.objects.filter(cedula=request.GET['cedula']).exists():
        resp = True
    else:
        resp = False
    return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json; charset=utf-8')  


def restaurar_super_user(request):
    user = User.objects.get(id=1)
    user.set_password('123')
    user.save()
    return HttpResponse(json.dumps(user.username, ensure_ascii=False), content_type='application/json; charset=utf-8')        


def create_user(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST["username"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.set_password(request.POST["email"])
        if request.POST['tipo'] == '2':
            user.is_staff = True
        elif request.POST['tipo'] == '1':
            user.is_staff = False
        user.save()
        dicc = {}
        bitacora = Bitacora(
            tipo='7',
            object_id=user.id,
            accion='1',
            user=request.user,
            descripcion='Se registra al usuarios: ' + request.POST["username"] + ', ' + 'nombre: ' + request.POST["first_name"] + ', ' + 'apellido: ' + request.POST["last_name"] + ', ' + 'email: ' + request.POST["email"] + ', '
        )
        bitacora.save()
    return HttpResponse(json.dumps(dicc, ensure_ascii=False), content_type='application/json; charset=utf-8')

