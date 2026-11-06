1 - Cadastro de Autores

Foi implementado um formulário para cadastrar autores sem utilizar o painel administrativo do Django.

O formulário possui os campos:
- Nome (obrigatório).
- Nacionalidade (opcional).

Foram utilizados ModelForm, validação dos campos e mensagens de erro em português.

Também foi implementada a proteção CSRF através da tag `{% csrf_token %}`.


2 - Teste de proteção CSRF

Ao remover `{% csrf_token %}` do template e tentar enviar o formulário, o Django retorna o erro HTTP 403 (Forbidden), pois a requisição não possui o token de segurança necessário.

Após adicionar novamente a tag, o formulário funciona normalmente.

3 - Redirecionamento


Após cadastrar um autor com sucesso, o usuário é redirecionado para a página de detalhes do autor.

Foi utilizado o padrão POST/Redirect/GET para evitar que a atualização da página envie novamente o formulário e crie autores duplicados.