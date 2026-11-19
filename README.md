### ====== FORMS - PARTE 1 ======

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


### ===== FORMS - ATIVIDADE SÁBADO LETIVO 1 =====

### 1.2 Perguntas

a) Não necessariamente. O LivroModelForm não precisa ser alterado, pois ele utiliza automaticamente as informações e validações definidas no Model. O Django identifica os validadores dos campos e os aplica durante a validação do formulário. Dessa forma, é possível manter as validações centralizadas, evitando repetir o mesmo código em diferentes partes do sistema.

b) Os validators são utilizados para verificar regras específicas de um valor, como tamanho mínimo, valor máximo ou formato de um dado.

Já o método clean_<campo>() permite criar validações personalizadas para um campo específico, aumentando a liberdade para analisar e modificar seu valor antes de salvá-lo. Ex.: verificar se o título de um livro possui uma palavra proibida. Essa regra pode ser implementada com clean_titulo(), pois exige uma lógica personalizada.

c) 
1. O título não pode ser igual ao nome do autor.**

Estratégia: clean().

Justificativa: essa validação precisa comparar dois campos diferentes do mesmo formulário (título e autor). Por isso, o método clean() é o mais adequado.

2. O título deve ser salvo sem espaços no início e no fim.

Estratégia: clean_<campo>.

Justificativa: permite utilizar o método strip() para remover os espaços em branco do início e do final do título antes de salvar o valor.

3. O número de páginas deve ser no máximo 5000.**

Estratégia: validators=[...].

Justificativa: podemos utilizar o MaxValueValidator(5000) para estabelecer um limite máximo de páginas, sem precisar criar uma validação personalizada.

4. Um livro "indisponível" precisa ter o ISBN preenchido.

Estratégia: clean().

Justificativa: essa regra depende da relação entre dois campos: a disponibilidade do livro e o ISBN. Portanto, precisamos verificar os dois valores ao mesmo tempo.
