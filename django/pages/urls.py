from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageHome.as_view(), name='home'),
    path('eventos/', views.PageEventos.as_view(), name='eventos'),
    path('reservas/', views.PageReservas.as_view(), name='reservas'),
    path('permissao-negada/', views.PageNoPerm.as_view(), name='noPerm')
]
