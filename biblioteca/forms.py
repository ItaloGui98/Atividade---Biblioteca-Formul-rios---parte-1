from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade']

        labels = {
            'nome': 'Nome',
            'nacionalidade': 'Nacionalidade',
        }

        error_messages = {
            'nome': {
                'required': 'O nome do autor é obrigatório.',
            }
        }