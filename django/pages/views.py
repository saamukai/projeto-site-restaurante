from django.views.generic import TemplateView

# Create your views here.
class PageHome (TemplateView):
    template_name = 'home.html'

class PageEventos (TemplateView):
    template_name = 'eventos.html'

class PageCardapio (TemplateView):
    template_name = 'cardapio.html'

class PageReservas (TemplateView):
    template_name = 'reservas.html'
