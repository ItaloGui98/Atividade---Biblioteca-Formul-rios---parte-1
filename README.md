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

3. O número de páginas deve ser no máximo 5000.

Estratégia: validators=[...].

Justificativa: podemos utilizar o MaxValueValidator(5000) para estabelecer um limite máximo de páginas, sem precisar criar uma validação personalizada.

4. Um livro "indisponível" precisa ter o ISBN preenchido.

Estratégia: clean().

Justificativa: essa regra depende da relação entre dois campos: a disponibilidade do livro e o ISBN. Portanto, precisamos verificar os dois valores ao mesmo tempo.

### 2.2 Perguntas

a) Se esquecermos request.FILES, o Django não receberá o arquivo enviado, fazendo com que a capa fique vazia, mesmo que tenha sido selecionada. Caso o enctype="multipart/form-data" também seja esquecido no formulário HTML, o navegador não enviará o arquivo corretamente ao servidor. Em ambos os casos, não apareceram avisos automáticos no formulário. O cadastro pode até funcionar, mas o livro ficará sem capa.

b) 
- STATICFILES_DIRS / {% static %}: são utilizados para arquivos estáticos do projeto, como CSS, JavaScript, ícones e imagens que fazem parte da interface.

- MEDIA_ROOT / .url: são utilizados para arquivos enviados pelos usuários, como as capas dos livros.
Na Mini Biblioteca, são utilizados arquivos estáticos para a aparência do sistema e arquivos de mídia para armazenar as capas cadastradas.

c) Isso acontece porque o Django, por padrão, não exclui automaticamente os arquivos físicos quando um registro é removido ou quando uma imagem é substituída. Tendo em vista o longo prazo, isso pode ocupar espaço desnecessário no servidor, acumulando arquivos que não são mais utilizados.

d) Porque um arquivo pode ter sua extensão alterada para .jpg ou .png sem realmente ser uma imagem. Dessa forma, o servidor também deve verificar o conteúdo real do arquivo, limitar seu tamanho, aceitar apenas formatos seguros, gerar nomes de arquivos adequados e impedir a execução de arquivos enviados, o que já se relaciona com os tipos de validação.

Erro ao arquivo não possuir extensão adequada: File extension “webp” is not allowed. Allowed extensions are: jpg, jpeg, png.

### 3.1 Perguntas

a) A própria CreateView controla os métodos GET e POST automaticamente. Quando o formulário é inválido, a página é exibida novamente com os erros de validação, permitindo que o usuário corrija as informações.

b) Porque a CreateView utiliza internamente os métodos do Django que já recebem os arquivos enviados pelo formulário. Assim, não se torna necessário passar request.FILES manualmente.

c) Porque o GET serve para exibir a confirmação, enquanto o POST confirma a ação de exclusão. Se a exclusão acontecesse em um GET, um simples acesso ao link poderia apagar o livro sem confirmação, causando exclusões acidentais.

d) Uma vantagem das CBVs é que elas reduzem de forma considerável a repetição de código, e oferecem funcionalidades prontas do Django. Uma desvantagem é que podem ser mais difíceis de entender inicialmente, principalmente quando possuem muitas heranças e métodos. Com isso, eu escolheria uma FBV quando precisasse implementar uma operação simples e específica, com pouca lógica e sem necessidade das funcionalidades de uma classe genérica.
