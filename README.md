
![logoFacul](https://user-images.githubusercontent.com/109771351/228919209-3b0e8d9c-bb31-425d-9e80-dd53180bcd6f.png)

# Curso de Engenharia de Software
![eng_Software_Simbol-removebg-preview](https://github.com/2000Paulo/P1-PROF-MARCIO/assets/109771351/4b5395f6-1d6c-4ecd-a1ac-9c4a32b6daca)

### Materia: Estrutura de Dados - Turma B - 3º período.
### Integrantes do Grupo: Paulo Victor Melo e Luan Santos.
### Professor: Marcio Garrido
*******************

<br>

# Fluxograma do Projeto


![image](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/050f824f-270e-4395-a673-598c8b784c3a)

Interface do Programa (Menu): Essa é a tela inicial do programa, onde o usuário terá diferentes opções para escolher.<br><br>O menu apresenta as seguintes opções:<br><br>
Cadastro de Animal: Ao selecionar essa opção, o fluxograma seguirá para a tela de cadastro dos animais.<br><br>
Cadastro de Candidato: Ao escolher essa opção, o fluxograma avançará para o processo de cadastro de candidatos interessados em adotar um animal.
Exibir Relatório: Se essa opção for selecionada, o fluxograma prosseguirá para a exibição de diferentes tipos de relatórios.

![image](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/3c8ab04a-61b9-412f-9377-ffb50ee1d95b)

Tela de Cadastro dos Animais: Nessa etapa, o usuário preencherá os dados relacionados ao animal que está sendo cadastrado.<br><br> 
Os dados solicitados podem incluir informações como a espécie do animal. Após fornecer essas informações, o fluxograma prossegue para o próximo passo.<br><br>
Inserir Dados Restantes do Animal: Nessa parte, o usuário será solicitado a inserir informações adicionais sobre o animal, como idade, cor, porte, particularidade e uma breve descrição.
Após preencher todos os dados, o fluxograma segue para o Dados no Banco de Dados, Nessa etapa, os dados referentes à geração do cadastro de animais serão salvos no banco de dados para futuras referências.
Logo após o  programa volta para o menu principal.

![image](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/2de03210-f2f7-436e-99b2-18cbd60ce6c9)
<br><br>
Cadastro de Candidato: Essa parte do fluxograma representa o processo de cadastro de pessoas interessadas em adotar um animal. O usuário será solicitado a inserir seus dados pessoais, como nome, CPF e e-mail. Além disso, será necessário inserir a espécie de interesse
e outras características do animal desejado.<br> Após preencher todas as informações, o fluxograma avança para o Dados no Banco de Dados, Nessa etapa, os dados referentes à geração do cadastro de candidatos para a adoção serão salvos no banco de dados para futuras referências.

### Logo após o  programa volta para o menu principal.

![image](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/c7f3184f-ea77-4524-a179-dd63e82606d1)

**Opção de Relatório:**<br>

Nessa parte, o usuário terá a opção de escolher entre diferentes tipos de relatórios. As opções podem incluir relatório da pessoa pesquisada pelo CPF, relatório de todos os animais cadastrados e relatório geral. Dependendo da escolha, o fluxograma seguirá para a respectiva opção selecionada.

**Ao digitar a opção 1:**<br>

Relatório Geral dos Candidatos com seus Animais Pareados: Essa parte do fluxograma representa a opção de geração de um relatório que apresenta os candidatos e os animais que foram pareados de acordo com as preferências e características informadas pelos candidatos. Esse relatório exibirá informações como o nome do candidato e o animal adotado.

**Ao digitar a opção 2:**<br>

Relatório da Pessoa Pesquisada por CPF: Se essa opção for escolhida, o fluxograma avançará para a exibição de um relatório específico contendo informações relacionadas à pessoa pesquisada pelo seu CPF, como o animal adotado.

**Ao digitar a opção 3:**<br>

Relatório de Todos os Animais Cadastrados: Se essa opção for selecionada, o fluxograma prosseguirá para a exibição de um relatório completo com informações de todos os animais cadastrados, como espécie, idade, cor e outros detalhes relevantes.

*******************

# Explicação do Código
### Para facilitar a Compreensão do código Explicaremos por partes...
*******************
#### 1 - Código de conexão e cadastro em um banco de dados SQLite:

- Nesse código, você importa o módulo sqlite3 para trabalhar com o banco de dados SQLite.
- Há duas partes distintas no código: a primeira parte realiza o cadastro de pessoas e a segunda parte realiza o cadastro de animais.
- Na primeira parte, você se conecta ao banco de dados utilizando sqlite3.connect('banco_de_dados.db').
- Em seguida, obtém o nome e a idade da pessoa através de entradas do usuário.
- Utilizando a função cur.execute(), você executa uma instrução SQL para inserir os dados da pessoa na tabela pessoas.
- Após o cadastro das pessoas, você fecha a conexão com o banco de dados.
- A segunda parte do código segue uma lógica semelhante para o cadastro de animais, onde são solicitadas informações sobre a cor, tamanho e idade do animal.
- Novamente, é utilizada a função cur.execute() para inserir os dados do animal na tabela animais.
- Por fim, você fecha a conexão com o banco de dados novamente.

#### 2 - Código de exibição de menu e cadastro de pessoas e animais:

- Nesse código, você define a função exibir_menu() que exibe um menu para o usuário com opções numéricas.
- A função utiliza um loop while True para manter o menu sendo exibido até que o usuário escolha a opção de sair.
- Dentro do loop, você verifica a escolha do usuário através da função isdigit() para garantir que seja um valor numérico.
- Dependendo da escolha do usuário, você chama as respectivas funções para cadastrar pessoas, cadastrar animais ou gerar um relatório.
- Para cadastrar pessoas, você instancia a classe Cadastro_pessoas e chama o método cadastro().
- Para cadastrar animais, você instancia a classe CadastroAnimais e chama o método cadastrar_animal().
- Para gerar um relatório, você exibe uma mensagem solicitando ao usuário que escolha entre um relatório geral ou uma pesquisa por nome.
- Com base na escolha do usuário, você instancia a classe Relatorio e chama os métodos gerar_relatorio() ou pesquisar_pessoa().

#### 3 - Código da classe Cadastro_pessoas:

- Nessa classe, você define o método __init__() que estabelece a conexão com o banco de dados no momento da criação do objeto.
- O método cadastro() é responsável por solicitar ao usuário as informações necessárias para cadastrar uma pessoa.
- As informações são obtidas através de entradas do usuário, como nome, idade, email, espécie de animal de preferência, cor do animal de preferência, idade do animal de preferência e particularidade do animal de preferência.
- Utilizando a função cur.execute(), você executa uma instrução SQL para inserir os dados da pessoa na tabela pessoas.
- Por fim, a conexão com o banco de dados é fechada.

#### 4 - Código da classe CadastroAnimais:

- Essa classe contém o método cadastrar_animal() que solicita ao usuário as informações necessárias para cadastrar um animal.
- Assim como no código anterior, as informações são obtidas através de entradas do usuário, como espécie, cor, idade e porte do animal.
- Utilizando a função cur.execute(), você executa uma instrução SQL para inserir os dados do animal na tabela animais.
- Por fim, a conexão com o banco de dados é fechada.

#### 5 - Código da classe Relatorio:

- Essa classe é responsável por gerar relatórios, pesquisar pessoas e adotar animais.
- O método __init__() estabelece a conexão com o banco de dados no momento da criação do objeto.
- O método gerar_relatorio() executa uma consulta SQL para buscar todas as pessoas cadastradas e seus respectivos animais de preferência.
- Para cada pessoa encontrada, é realizada outra consulta SQL para buscar animais compatíveis no banco de dados.
- Se houver animais compatíveis, suas informações são exibidas. Caso contrário, é exibida uma mensagem informando que não foram encontrados animais compatíveis.
- O método pesquisar_pessoa(nome_pessoa) busca uma pessoa específica pelo nome e exibe informações sobre a pessoa e os animais compatíveis.
- O método adotar_animal(especie_animal) remove um animal do banco de dados com base no número de identificação.
- O método fechar_conexao() fecha a conexão com o banco de dados.

#### 6 - Código de inicialização do menu:

- Esse trecho de código chama a função exibir_menu() para iniciar o programa e exibir o menu principal.
