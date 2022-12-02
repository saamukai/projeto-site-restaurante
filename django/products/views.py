from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . import models
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.

## PRODUCTS CREATE
class CategoriaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    fields = ['nome', 'disponivel']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'disponivel']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")

## UPDATE PRODUCTS
class CategoriaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    fields = ['nome']
    template_name = 'cadastros/formcategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    fields = ['nome', 'descricao', 'preco', 'categoria', 'disponivel']
    template_name = 'cadastros/formprod.html'
    success_url = reverse_lazy("cardapio")


## PRODUCTS DELETE
class CategoriaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    template_name = 'cadastros/deletecategoria.html'
    success_url = reverse_lazy("lista-categoria")

class ProdutoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    template_name = 'cadastros/formproddelete.html'
    success_url = reverse_lazy("cardapio")

## LIST VIEW
class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('noPerm')
    model = models.Categoria
    template_name = 'listas/categorialist.html'

class ProdutoList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    group_required = u'Gerente'
    login_url = reverse_lazy('noPerm')
    model = models.Produto
    template_name = 'listas/produtoslist.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['categorias'] = models.Categoria.objects.all()
        return context
    def get_queryset(self):
        return super().get_queryset().order_by('nome')

class CardapioList(ListView):
    model = models.Produto
    template_name = 'listas/cardapio.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['categorias'] = models.Categoria.objects.filter(disponivel=True).order_by('nome')
        return context
    def get_queryset(self):
        return super().get_queryset().order_by('nome')

def categoriaDisponivel (request, ID):
    categoria = models.Categoria.objects.get(pk=ID)
    categoria.disponivel = False if categoria.disponivel == True else True
    categoria.save()
    return redirect('lista-categoria')

def produtoDisponivel (request, ID):
    produto = models.Produto.objects.get(pk=ID)
    produto.disponivel = False if produto.disponivel == True else True
    produto.save()
    return redirect('lista-produtos')
