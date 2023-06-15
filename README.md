
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
### Para facilitar a Compreensão dividimos a Explicação por Classes...
*******************
#### 1 - Animais:

![part1](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/6564add7-2036-46cd-b8f5-cb1582c1b103)

- Nesta parte, importamos o módulo sqlite3 e definimos a classe CadastroAnimais. O método __init__ é o construtor da classe e estabelece uma conexão com o banco de dados SQLite chamado banco_de_dados.db. Ele também cria um cursor que será usado para executar comandos SQL no banco de dados.

![part2](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/924079a8-5b40-4fd5-bb85-8e8d15641de4)

- Esta parte contém o método exibir_animais_adotados. Ele define uma lista de animais e, em seguida, utiliza um loop para exibir os animais em um formato de caixa na saída.

![part3](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/ed8b1bbf-fc98-421e-9cbf-ea7e337dbdfd)

- Nesta parte, o método cadastrar_animal é definido. Ele contém um loop infinito while True que permite ao usuário fazer várias tentativas até fornecer uma entrada válida. A função exibir_animais_adotados é chamada para exibir os animais disponíveis. Em seguida, o usuário é solicitado a escolher um número de animal. O código trata exceções caso o número fornecido não seja válido.

- Dentro do bloco try, podem ser inseridos mais trechos de código para solicitar informações adicionais do animal e inserir os dados no banco de dados.

- Essas são as três principais partes do código, cada uma com uma funcionalidade específica: configuração do banco de dados, exibição dos animais adotados e cadastro de um novo animal.

#### 2 - Pessoas:

![part1](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/9a388375-3106-453a-b1e6-8bddae80e2ea)

- Nesta parte, importamos o módulo sqlite3 e a biblioteca animais. Em seguida, definimos a classe Cadastro_pessoas. O método __init__ é o construtor da classe e estabelece uma conexão com o banco de dados SQLite chamado banco_de_dados.db. Ele também cria um cursor que será usado para executar comandos SQL no banco de dados.

![part2](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/f2490fdf-915a-4b01-9a2e-6b0ff66cd59a)

- Nessa parte, o código solicita ao usuário as informações pessoais da pessoa a ser cadastrada. São solicitados o nome, a idade e o email, e esses valores são armazenados nas variáveis nome, idade e email, respectivamente.

![part3](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/478a89d3-5383-4654-9313-930c3fed1cff)

- o código lida com a escolha do animal de preferência da pessoa. É criada uma lista animais_disponiveis contendo os animais disponíveis para escolha. Em seguida, essa lista é percorrida com um loop for e cada animal é exibido na tela com seu número correspondente.

- O usuário é solicitado a digitar o número do animal de preferência da pessoa. Esse valor é convertido para inteiro e é feita uma verificação para garantir que seja uma escolha válida, ou seja, um número entre 1 e o número total de animais disponíveis.

- Depois, a variável animal_escolhido recebe o animal selecionado com base no número escolhido pelo usuário.

![part4](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/719c3ebc-d565-4395-bf69-d9a20e91347d)

- o código lida com o cadastro das informações no banco de dados. São solicitadas informações adicionais sobre o animal de preferência da pessoa, como cor, idade e particularidade, que são armazenadas nas variáveis cor, idade_animal e particularidade.

- Em seguida, é executada uma instrução SQL para inserir todas as informações no banco de dados, utilizando os valores obtidos anteriormente. Após a inserção, a conexão com o banco de dados é fechada e uma mensagem de sucesso é exibida. Em caso de erro durante o cadastro, é exibida uma mensagem de erro específica.

#### 3 - Relatorio:

![part1](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/031be056-b65e-4f1c-926b-f57fd911b76a)

- Essas são declarações de importação que trazem os módulos necessários para trabalhar com bancos de dados SQLite (sqlite3) e gerar números aleatórios (random).

![part2](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/d8278ad5-f4dc-40da-be7a-422c2c3f27d0)

- Este código define uma classe chamada Relatorio que representa um relatório. No método __init__, a classe estabelece uma conexão com o banco de dados SQLite especificado pelo arquivo banco_de_dados.db e cria um objeto cursor para executar consultas SQL.

![part3](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/640d99f6-5c49-4c42-bee9-ffa32b8755d3)

- Este método, gerar_relatorio, executa uma consulta SQL para recuperar as informações de pessoas da tabela pessoas. Em seguida, itera sobre cada pessoa e executa outra consulta para obter animais compatíveis com base na espécie, cor e idade da pessoa. O método imprime o perfil da pessoa e, em seguida, os animais compatíveis, se houver algum.

![part4](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/4b8bf616-1f5c-4470-b621-29eafc8a9f6b)

- Este método, pesquisar_pessoa, recebe um nome de pessoa como argumento e executa uma consulta SQL para pesquisar essa pessoa na tabela pessoas. Se a pessoa for encontrada, o método imprime as informações da pessoa e busca animais compatíveis com base nas mesmas características. Em seguida, exibe os animais compatíveis, se houver algum. Caso contrário, exibe uma mensagem informando que não foram encontrados animais compatíveis.

![part5](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/7d13e90b-81d6-41a9-9324-9e8892ae8519)

- Este método, adotar_animal, recebe a espécie de animal como argumento e gera um ID de animal aleatório de 4 dígitos. Em seguida, executa uma consulta SQL para excluir o animal com o ID gerado da tabela animais. Por fim, o método confirma as alterações feitas no banco de dados.

![part6](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/975e7f03-c7ea-4c7f-86fd-db4b3686fd46)

- Este método, fechar_conexao, é responsável por fechar a conexão com o banco de dados chamando o método close() no objeto de conexão (self.con).

- Em resumo, o código define uma classe chamada Relatorio que realiza operações de geração de relatórios, pesquisa de pessoas, adoção de animais e gerenciamento da conexão com o banco de dados SQLite. Cada método da classe executa consultas SQL no banco de dados para recuperar e manipular informações.

#### 4 - main:

![part1](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/204921c9-0b6e-4a01-9481-ca054ebc6e26)

- Essas são declarações de importação que importam as classes e módulos necessários para o programa funcionar. O código está importando as classes Cadastro_pessoas, CadastroAnimais e Relatorio de arquivos chamados animais.py, pessoas.py e relatorio.py, respectivamente. Além disso, o código importa o módulo sqlite3 para trabalhar com bancos de dados SQLite.

![part2](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/1a76f60c-b8a2-4947-a202-216f38d0fdd3)

- Esta função contém o loop principal do menu, que continuará sendo executado até que o usuário escolha a opção para sair do programa. O loop permite que o usuário selecione diferentes opções do menu e execute as operações correspondentes.

![part3](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/fefa0f78-5d24-42fe-90b0-c4322eba0a04)

- Esta parte do código verifica se a escolha do usuário é um número válido. Se for um número válido, o código converte a escolha para um inteiro e executa o bloco correspondente à opção selecionada.

- Se a escolha for 1, cria-se um objeto da classe Cadastro_pessoas e chama-se o método cadastro para cadastrar uma pessoa.
- Se a escolha for 2, cria-se um objeto da classe CadastroAnimais e chama-se o método cadastrar_animal

![part4](https://github.com/2000Paulo/save_the_animals-project/assets/109771351/795bb258-6844-4907-8faf-9a1b47b41650)

- Esta linha verifica se o arquivo está sendo executado diretamente como um programa principal. O código dentro desse bloco só será executado se o arquivo for o ponto de entrada principal.

- Essa verificação é útil quando você tem um módulo que pode ser importado por outros módulos, mas também pode ser executado diretamente. Nesse caso, se o arquivo for importado como um módulo, o bloco if __name__ == "__main__": será ignorado e as definições de função e classe serão importadas normalmente. No entanto, se o arquivo for executado diretamente, ou seja, se for o programa principal, o bloco if __name__ == "__main__": será executado e a função exibir_menu() será chamada para iniciar o programa.
