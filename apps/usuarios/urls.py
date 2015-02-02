from django.conf.urls import patterns, url
from apps.usuarios.views import listarPermisos, crearPermisos, listarPermisosPagina, eliminarPermisos, editarPermisos, verPermisos, listarRoles, listarRolesPagina, crearRoles, eliminarRoles

urlpatterns = patterns('',

    url(r'^permisos/$', listarPermisos),
    url(r'^permisos/(?P<num_pagina>\d+)/$', listarPermisosPagina),
    url(r'^permisos/(?P<num_pagina>\d+)/crear/$', crearPermisos),
    url(r'^permisos/(?P<num_pagina>\d+)/eliminar/(?P<id_permiso>\d+)/$', eliminarPermisos),
    url(r'^permisos/(?P<num_pagina>\d+)/editar/(?P<id_permiso>\d+)/$', editarPermisos),
    url(r'^permisos/(?P<num_pagina>\d+)/ver/(?P<id_permiso>\d+)/$', verPermisos),
    url(r'^roles/$', listarRoles),
    url(r'^roles/(?P<num_pagina>\d+)/$', listarRolesPagina),
    url(r'^roles/(?P<num_pagina>\d+)/crear/$', crearRoles),
    url(r'^roles/(?P<num_pagina>\d+)/eliminar/(?P<id_rol>\d+)/$', eliminarRoles),

)