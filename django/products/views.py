from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models
from django.urls import reverse_lazy
# Create your views here.


## PRODUCTS CREATE
class CategoriaCreate(CreateView):
    model = models.Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoCreate(CreateView):
    model = models.Produto
    fields = ['nome', 'descricao', 'preco', 'disponivel', 'categoria']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")

## UPDATE PRODUCTS
class CategoriaUpdate(UpdateView):
    model = models.Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoUpdate(UpdateView):
    model = models.Produto
    fields = ['nome', 'descricao', 'preco', 'disponivel', 'categoria']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")


## PRODUCTS DELETE
class CategoriaDelete(DeleteView):
    model = models.Categoria
    template_name = 'cadastros/formcategoriadelete.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoDelete(DeleteView):
    model = models.Produto
    template_name = 'cadastros/formproddelete.html'
    success_url = reverse_lazy("cardapio")

## LIST VIEW
class CategoriaList(ListView):
    model = models.Categoria
    template_name = 'listas/categorialist.html'

class ProdutoList(ListView):
    model = models.Produto
    template_name = 'listas/cardapio.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['categorias'] = models.Categoria.objects.all()
        return context
