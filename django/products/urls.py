from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-categoria/', views.CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path('cadastrar-produto/', views.ProdutoCreate.as_view(), name="cadastrar-produto"),
    path('editar-categoria/<int:pk>', views.CategoriaUpdate.as_view(), name="editar-categoria"),
    path('editar-produto/<int:pk>', views.ProdutoUpdate.as_view(), name="editar-produto"),
    path('deletar-categoria/<int:pk>', views.CategoriaDelete.as_view(), name="editar-categoria"),
    path('deletar-produto/<int:pk>', views.ProdutoDelete.as_view(), name="editar-produto"),
]
