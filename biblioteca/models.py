from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator, FileExtensionValidator
from django.utils import timezone
from .validators import validar_tamanho_arquivo


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50,blank=True) 

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.nome

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(3)])

    autores = models.ManyToManyField( #ligação de muitos para muitos entre Livro e autor
        Autor, 
        related_name='livros', 
        blank=True
    )

    categoria = models.ManyToManyField(
        Category, 
        related_name='books', 
        blank=True
    )

    ano_publicacao = models.IntegerField(validators=[MinLengthValidator(1450), MaxValueValidator(timezone.now().year)])
    paginas = models.IntegerField(validators=[MinLengthValidator(1), MaxValueValidator(5000)], null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    isbn = models.CharField(max_length=13, validators=[RegexValidator(regex=r'^\d{13}$',message='O ISBN deve conter exatamente 13 dígitos.')], null=True, blank=True)
    capa = models.ImageField(upload_to='capas/', validators=[validar_tamanho_arquivo, FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], null=True, blank=True)
    def __str__(self):
        return self.titulo