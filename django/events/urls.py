from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageEventos.as_view(), name='eventos'),
]
