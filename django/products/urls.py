from django.urls import path
from . import views

urlpatterns = [
    # CREATE
    path('cadastrar-categoria/', views.CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path('cadastrar-produto/', views.ProdutoCreate.as_view(), name="cadastrar-produto"),

    # UPDATE
    path('renomear-categoria/<int:pk>', views.CategoriaUpdate.as_view(), name="editar-categoria"),
    path('editar-produto/<int:pk>', views.ProdutoUpdate.as_view(), name="editar-produto"),
    path('categorias/disponibilidade-categoria/<int:ID>', views.categoriaDisponivel, name="categoria-disponivel"),
    path('disponibilidade-produto/<int:ID>', views.produtoDisponivel, name="produto-disponivel"),


    # DELETE
    path('deletar-categoria/<int:pk>', views.CategoriaDelete.as_view(), name="deletar-categoria"),
    path('deletar-produto/<int:pk>', views.ProdutoDelete.as_view(), name="deletar-produto"),

    # LISTAS
    path('', views.ProdutoList.as_view(), name="lista-produtos"),
    path('categorias/', views.CategoriaList.as_view(), name="lista-categoria"),
    path('cardapio/', views.CardapioList.as_view(), name="cardapio"),
]
