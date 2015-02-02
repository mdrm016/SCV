from django import forms
from .models import Permisos, Rol
from django.core import validators
from django.core.exceptions import ValidationError

def validate_nombre_permiso_unique(value):
    if Permisos.objects.filter(nombre=value).exists():
        raise ValidationError(u'El nombre de permiso "%s" ya existe y no puede haber duplicados.' % value)
    
def validate_nombre_rol_unique(value):
    if Rol.objects.filter(nombre=value).exists():
        raise ValidationError(u'El nombre de Rol "%s" ya existe y no puede haber duplicados.' % value)
    
def getPermisos():
    permisos = Permisos.objects.all()
    perm = []
    for permiso in permisos:
        tupla = (permiso.nombre, permiso.nombre)
        perm.append(tupla)
    return perm
    
class PermisosForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, required=True, validators=[validate_nombre_permiso_unique])
    
class RolesForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, required=True, validators=[validate_nombre_rol_unique])
    descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 500, error_messages={'max_length': 'Longitud maxima: 500 caracteres'})
    permisos = forms.MultipleChoiceField(choices=getPermisos(), widget=forms.CheckboxSelectMultiple(), required=True, error_messages={'required': 'Debe seleccionar los permisos asociados al rol.'})
    