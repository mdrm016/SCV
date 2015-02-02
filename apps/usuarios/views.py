from .models import Permisos, Rol, RolPermiso
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .forms import PermisosForm, RolesForm
from django.core import serializers
from apps.utilidades.views import pagination, columnaRoles

# Create your views here.
""" Todas las funcionalidades del apartado registro"""
#Permisos
def listarPermisos(request):
    
    num_pagina = 1
    permisos = Permisos.objects.all()  
    pag = pagination(permisos, num_pagina)
    url_string = '/permisos/%s/crear/' % num_pagina
    ctx = {'url': url_string, 'registro': True}
    ctx.update(pag)
    template_name = 'vistas/usuarios/permisos.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listarPermisosPagina(request, num_pagina):
    
    permisos = Permisos.objects.all()      
    pag = pagination(permisos, num_pagina)
    url_string = '/permisos/%s/crear/' % num_pagina
    ctx = {'url': url_string, 'registro': True}
    ctx.update(pag)
    template_name = 'vistas/usuarios/permisos.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def crearPermisos(request, num_pagina):
    
    notificacion = ''
    tipo = ''
    abrev = ''
    ctx = {}
    if request.method == 'POST':
        form = PermisosForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['nombre'] 
            permiso = Permisos()
            permiso.nombre = nombre
            permiso.save()
            notificacion = 'Permiso "%s" creado exitosamente.' % nombre
            tipo = 'alert-success'
            abrev = 'Hecho!'
            template_name='vistas/usuarios/permisos.html'
        else:
            """notificacion = 'Hubo un error al crear el Permiso.'
            tipo = 'alert-danger'
            abrev = 'Error'"""
            template_name='vistas/usuarios/modal_crear_perm.html'
          
        ctx = pagination(Permisos.objects.all(), num_pagina)
        notificaciones ={'notificacion': notificacion, 'tipo': tipo, 'abrev': abrev, 'form': form}
        ctx.update(notificaciones)
        
    else:
        #print request
        form = PermisosForm()
        #data = serializers.serialize('json', form)
        #print data
        ctx ={'form': form}      
        template_name='vistas/usuarios/modal_crear_perm.html'
        #return HttpResponse(data, content_type='application/json')
        
    url_string = '/permisos/%s/crear/' % num_pagina
    url = {'url': url_string }
    ctx.update(url)    
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def eliminarPermisos(request, num_pagina, id_permiso):
    
    try:
        permiso = Permisos.objects.get(id=id_permiso)
        permiso.delete()
        notificacion = 'El permiso "%s" se ha eliminado correctamente.' % permiso.nombre
        tipo = 'alert-success'
        abrev = 'Eliminado!'
          
    except:
        notificacion = 'Hubo un error al eliminar el Permiso.'
        tipo = 'alert-danger'
        abrev = 'Error'
        
    template_name='vistas/usuarios/permisos.html'
    ctx = pagination(Permisos.objects.all(), num_pagina)
    notificaciones ={'notificacion': notificacion, 'tipo': tipo, 'abrev': abrev}
    ctx.update(notificaciones)
    url_string = '/permisos/%s/crear/' % num_pagina
    url = {'url': url_string }
    ctx.update(url)   
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def editarPermisos (request, num_pagina, id_permiso):
    
    id_permiso = int(id_permiso)
    permiso = Permisos.objects.get(id=id_permiso)
    ctx = {}
    if request.method == 'POST':
        form = PermisosForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['nombre'] 
            permiso = Permisos.objects.get(id=id_permiso)
            permiso.nombre = nombre
            permiso.save()
            notificacion = 'Permiso "%s" editado exitosamente.' % nombre
            tipo = 'alert-success'
            abrev = 'Hecho!'
            template_name='vistas/usuarios/permisos.html'
        else:
            """notificacion = 'Hubo un error al editar el Permiso.'
            tipo = 'alert-danger'
            abrev = 'Error'"""
            template_name='vistas/usuarios/modal_editar_perm.html'
          
        ctx = pagination(Permisos.objects.all(), num_pagina)
        notificaciones ={'notificacion': notificacion, 'tipo': tipo, 'abrev': abrev, 'form': form, 'permiso': permiso}
        ctx.update(notificaciones)
        
    else:
        form = PermisosForm()
        ctx ={'form': form, 'permiso': permiso}      
        template_name='vistas/usuarios/modal_editar_perm.html'
        
    url_string = '/permisos/%s/editar/%s/' % (num_pagina, id_permiso) 
    url = {'url': url_string }
    ctx.update(url)    
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def verPermisos (request, num_pagina, id_permiso):
    
    id_permiso = int(id_permiso)
    permiso = Permisos.objects.get(id=id_permiso)    
    pag = pagination(Permisos.objects.all(), num_pagina)
    url_string = '/permisos/%s/editar/%s/' % (num_pagina, id_permiso)
    ctx ={'permiso': permiso, 'url': url_string}      
    ctx.update(pag)
    template_name='vistas/usuarios/modal_ver_perm.html'    
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

#Roles
def listarRoles(request):
    
    num_pagina = 1
    roles = Rol.objects.all()  
    pag = pagination(roles, num_pagina)
    url_string = '/roles/%s/crear/' % num_pagina
    ctx = {'url': url_string, 'registro': True}
    ctx.update(pag)
    template_name = 'vistas/usuarios/roles.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listarRolesPagina(request, num_pagina):
    
    roles = Rol.objects.all()      
    pag = pagination(roles, num_pagina)
    url_string = '/roles/%s/crear/' % num_pagina
    ctx = {'url': url_string, 'registro': True}
    ctx.update(pag)
    template_name = 'vistas/usuarios/roles.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def crearRoles(request, num_pagina):
    
    notificacion = ''
    tipo = ''
    abrev = ''
    ctx = {}
    permisosChk =''
    if request.method == 'POST':
        form = RolesForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            permisos = form.cleaned_data['permisos']
            rol = Rol()
            rol.nombre = nombre
            rol.descripcion = descripcion
            rol.save()
            for permiso in permisos:
                objPerm = Permisos.objects.get(nombre=permiso)
                rol_permiso = RolPermiso(rol=rol, permiso=objPerm)
                rol_permiso.save() 
            notificacion = 'Rol "%s" creado exitosamente.' % nombre
            tipo = 'alert-success'
            abrev = 'Hecho!'
            template_name='vistas/usuarios/roles.html'
        else:
            """notificacion = 'Hubo un error al crear el Rol.'
            tipo = 'alert-danger'
            abrev = 'Error'"""
            template_name='vistas/usuarios/modal_crear_rol.html'
            try:
                permisosChk = form.cleaned_data['permisos']
            except:
                permisosChk = ''
            
        elementCheck = columnaRoles(Permisos.objects.all())  
        ctx = pagination(Rol.objects.all(), num_pagina)
        notificaciones ={'notificacion': notificacion, 'tipo': tipo, 'abrev': abrev, 'elementCheck': elementCheck, 'form': form, 'permisosChk':permisosChk}
        ctx.update(notificaciones)
        
    else:
        form = RolesForm()
        elementCheck = columnaRoles(Permisos.objects.all())  
        ctx ={'form': form, 'elementCheck': elementCheck}      
        template_name='vistas/usuarios/modal_crear_rol.html'
        
    url_string = '/roles/%s/crear/' % num_pagina
    url = {'url': url_string }
    ctx.update(url)    
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def eliminarRoles(request, num_pagina, id_rol):
    
    try:
        rol = Rol.objects.get(id=id_rol)
        rol.delete()
        notificacion = 'El permiso "%s" se ha eliminado correctamente.' % rol.nombre
        tipo = 'alert-success'
        abrev = 'Eliminado!'
          
    except:
        notificacion = 'Hubo un error al eliminar el Permiso.'
        tipo = 'alert-danger'
        abrev = 'Error'
        
    template_name='vistas/usuarios/roles.html'
    ctx = pagination(Rol.objects.all(), num_pagina)
    notificaciones ={'notificacion': notificacion, 'tipo': tipo, 'abrev': abrev}
    ctx.update(notificaciones)
    url_string = '/roles/%s/crear/' % num_pagina
    url = {'url': url_string }
    ctx.update(url)   
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
