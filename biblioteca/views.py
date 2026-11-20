from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Livro, Autor
from .forms import AutorForm, LivroForm


# LISTAGEM DE LIVROS
class LivroListView(ListView):
    model = Livro
    template_name = 'biblioteca/listar_livros.html'
    context_object_name = 'livros'
    ordering = ['titulo']

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['autores'] = Autor.objects.all()

        return contexto


# DETALHES DO AUTOR
class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor.html'
    context_object_name = 'autor'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['livros'] = self.object.livros.all()

        return contexto


# CADASTRO DE AUTOR
class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/novo_autor.html'
    success_url = reverse_lazy('listar_livros')


# CADASTRO DE LIVRO
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/forms/form_livros.html'
    success_url = reverse_lazy('listar_livros')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo_pagina'] = 'Novo livro'
        contexto['texto_botao'] = 'Cadastrar livro'

        return contexto


# EDIÇÃO DE LIVRO
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/forms/form_livros.html'
    context_object_name = 'livro'
    success_url = reverse_lazy('listar_livros')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo_pagina'] = 'Editar livro'
        contexto['texto_botao'] = 'Salvar alterações'

        return contexto


# EXCLUSÃO DE LIVRO
class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_delete.html'
    context_object_name = 'livro'
    success_url = reverse_lazy('listar_livros')


# PÁGINA SOBRE
class SobreView(TemplateView):
    template_name = 'biblioteca/sobre.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['total_livros'] = Livro.objects.count()

        contexto['livros_disponiveis'] = Livro.objects.filter(
            disponivel=True
        ).count()

        return contexto

""" from django.shortcuts import get_object_or_404, render, redirect
from .models import Livro, Autor
from .forms import AutorForm, LivroForm

def listar_livros(request):
    livros = Livro.objects.all()
    autores = Autor.objects.all()

    return render(request, 'biblioteca/listar_livros.html', {'livros': livros, 'autores': autores})

def autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    livros = autor.livros.all()
    return render(request, 'biblioteca/autor.html', {'autor': autor, 'livros': livros})

def novo_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)

        if form.is_valid():
            autor = form.save()

            return redirect('listar_livros')

    else:
        form = AutorForm()

    return render(request, 'biblioteca/novo_autor.html', {
        'form': form
    })

def cadastrar_editar_livro(request, livro_id=None):
    if livro_id:
        livro = get_object_or_404(Livro, id=livro_id)
    else:
        livro = None

    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            livro_salvo = form.save()

            return redirect(
                'autor',
                id=livro_salvo.autores.first().id
            )

    else:
        form = LivroForm(instance=livro)

    contexto = {
        'form': form,
        'titulo_pagina': 'Editar livro' if livro else 'Novo livro',
        'texto_botao': 'Salvar alterações' if livro else 'Cadastrar livro',
    }

    return render(request, 'biblioteca/forms/form_livros.html', contexto)
"""