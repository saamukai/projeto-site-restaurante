from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.


## PRODUCTS CREATE
class CategoriaCreate(CreateView):
    model = models.Categoria
    fields = ['nome']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("cardapio")

class ProdutoCreate(CreateView):
    model = models.Produto
    fields = ['numero','nome', 'descricao', 'preco', 'disponivel', 'categoria']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")

## UPDATE PRODUCTS
class CategoriaUpdate(UpdateView):
    model = models.Categoria
    fields = ['nome']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("cardapio")

class ProdutoUpdate(UpdateView):
    model = models.Produto
    fields = ['numero','nome', 'descricao', 'preco', 'disponivel', 'categoria']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")


## PRODUCTS DELETE
class CategoriaDelete(DeleteView):
    model = models.Categoria
    fields = ['nome']
    success_url = reverse_lazy("cardapio")

class ProdutoDelete(DeleteView):
    model = models.Produto
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")
