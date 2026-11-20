from django.core.exceptions import ValidationError


def validar_tamanho_arquivo(arquivo):
    limite = 1 * 1024 * 1024  # 1 MB em bytes

    if arquivo.size > limite:
        raise ValidationError(
            'O tamanho da capa não pode ultrapassar 1 MB.'
        )