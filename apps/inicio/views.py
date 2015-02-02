from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template import RequestContext

class Autenticacion(TemplateView):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            template_name = 'vistas/inicio/index.html'
            ctx = {'inicio': True}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))