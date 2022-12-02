from django.views.generic import TemplateView

# Create your views here.
class PageHome (TemplateView):
    template_name = 'pages_guest/home.html'

class PageReservas (TemplateView):
    template_name = 'pages_guest/reservas.html'

class PageNoPerm (TemplateView):
    template_name = 'pages_guest/noPerm.html'
