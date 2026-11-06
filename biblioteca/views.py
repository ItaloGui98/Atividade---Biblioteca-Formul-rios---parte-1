from django.shortcuts import get_object_or_404, render, redirect
from .models import Livro, Autor
from .forms import AutorForm

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