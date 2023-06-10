from animais import *
from pessoas import *
from relatorio import *
import sqlite3


def exibir_menu():
    while True:
        print("╔════════════════════════════╗")
        print("║   Bem-vindo(a) ao Sistema  ║")
        print("║        de Cadastro!        ║")
        print("╠════════════════════════════╣")
        print("║ Por favor, selecione uma   ║")
        print("║    das opções abaixo:      ║")
        print("║                            ║")
        print("║ 1. Cadastrar Pessoas       ║")
        print("║ 2. Cadastrar Animal        ║")
        print("║ 3. Relatório               ║")
        print("║ 4. Sair/Exit               ║")
        print("╚════════════════════════════╝")

        escolha = input('')

        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 1:
                cadastrar = Cadastro_pessoas()
                cadastrar.cadastro()
            elif escolha == 2:
                cadastro_animal = CadastroAnimais()
                cadastro_animal.cadastrar_animal()
            elif escolha == 3:
                print('Digite 1 para o relatório geral e 2 para pesquisar por nome:')
                pes = int(input(''))
                if pes == 1:
                    relatorio = Relatorio()
                    relatorio.gerar_relatorio()
                elif pes == 2:
                    nome_p = input('Digite o nome da pessoa: ')
                    relatorio = Relatorio()
                    relatorio.pesquisar_pessoa(nome_p)
                    dig = int(input('Digite o número do animal que você deseja adotar: '))
                    relatorio.adotar_animal(dig)
            elif escolha == 4:
                break
            else:
                print('Opção inválida. Tente novamente.')
        else:
            print('Opção inválida. Tente novamente.')

        print()  # Linha em branco para separar as iterações do menu


if __name__ == "__main__":
    exibir_menu()
