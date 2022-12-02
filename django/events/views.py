from django.views.generic import TemplateView

# Create your views here.
class PageEventos (TemplateView):
    template_name = 'eventos/eventos.html'
