from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageHome.as_view(), name='home'),
    path('eventos/', views.PageEventos.as_view(), name='eventos'),
    path('cardapio/', views.PageCardapio.as_view(), name='cardapio'),
    path('reservas/', views.PageReservas.as_view(), name='reservas'),
]
