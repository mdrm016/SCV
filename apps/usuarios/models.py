from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

def get_file_path(instance, filename):
    import uuid
    import os

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/imagenes/', filename)
    
class Permisos(models.Model):
    
    nombre = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.nombre
    
class Rol(models.Model):
    
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    permisos = models.ManyToManyField(Permisos, through='RolPermiso', through_fields=('rol', 'permiso'))
    
    def __unicode__(self):
        return self.nombre
    
class RolPermiso(models.Model):
    
    rol = models.ForeignKey(Rol)
    permiso = models.ForeignKey(Permisos)
    
class Usuarios(models.Model):
    CATEGORIA = (
        ('CON', 'Controladores'),
        ('COB', 'Cobradores'),
        ('VER', 'Verificadores'),
        ('VEN', 'Vendedores'),
    )
    
    usuario = models.OneToOneField(User, primary_key=True)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    models.ImageField(upload_to=get_file_path, max_length=150, default='no-img.jpg', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    rol = models.ForeignKey(Rol)
    
    def __unicode__(self):
        return self.usuario.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuarios.objects.create(usuario=instance)
            
post_save.connect(create_user_profile, sender=User)
