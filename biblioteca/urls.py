from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import LivroListView, AutorDetailView, AutorCreateView, LivroCreateView, LivroUpdateView, LivroDeleteView, SobreView


urlpatterns = [
    path('', LivroListView.as_view(), name='listar_livros'),

    path('autor/<int:id>/', AutorDetailView.as_view(), name='autor'),

    path('autor/novo/', AutorCreateView.as_view(), name='novo_autor'),

    path('livro/novo/', LivroCreateView.as_view(), name='cadastrar_livro'),

    path('livro/<int:pk>/editar/', LivroUpdateView.as_view(), name='editar_livro'),

    path('livro/<int:pk>/excluir/', LivroDeleteView.as_view(), name='excluir_livro'),

    path('sobre/', SobreView.as_view(), name='sobre'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
