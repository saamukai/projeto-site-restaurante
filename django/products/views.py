from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.


## PRODUCTS CREATE
class CategoriaCreate(GroupRequiredMixin, CreateView):
    group_required = 'Administrador'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    fields = ['nome']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoCreate(GroupRequiredMixin, CreateView):
    group_required = 'Administrador'
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    fields = ['nome', 'descricao', 'preco', 'disponivel', 'categoria']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")

## UPDATE PRODUCTS
class CategoriaUpdate(GroupRequiredMixin, UpdateView):
    group_required = 'Administrador'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    fields = ['nome']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    fields = ['nome', 'descricao', 'preco', 'disponivel', 'categoria']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")


## PRODUCTS DELETE
class CategoriaDelete(GroupRequiredMixin, DeleteView):
    group_required = 'Administrador'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    template_name = 'cadastros/formcategoriadelete.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoDelete(GroupRequiredMixin, DeleteView):
    group_required = 'Administrador'
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    template_name = 'cadastros/formproddelete.html'
    success_url = reverse_lazy("cardapio")

## LIST VIEW
class CategoriaList(GroupRequiredMixin, ListView):
    group_required = 'Administrador'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    template_name = 'listas/categorialist.html'

class ProdutoList(ListView):
    model = models.Produto
    template_name = 'listas/cardapio.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['categorias'] = models.Categoria.objects.all()
        return context
