from django.conf.urls import patterns, url
from .views import Autenticacion

urlpatterns = patterns('',

	url(r'^$', 'django.contrib.auth.views.login', 
		{'template_name':'vistas/inicio/login.html'}, name='login'),

	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

	url(r'^index/$', Autenticacion.as_view(), name='inicio'),
)