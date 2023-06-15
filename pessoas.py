from animais import *
import sqlite3
class Cadastro_pessoas:
    def __init__(self):
        self.con = sqlite3.connect('banco_de_dados.db')
        self.cur = self.con.cursor()

    def cadastro(self):
        try:

            while True:
                    nome = input("Digite o seu nome : ")
                    print('\n')
                    if not nome.replace(" ", "").isalpha(): 
                        print("Nome inválido. Digite apenas letras.")
                        print("\n")
                    else:
                        break
                    
                    
            while True:
                    try:
                        cpf = int(input("Digite o seu cpf: (apanas numero!) "))
                        print('\n')
                        break
                    except ValueError:
                        print("Idade inválida. Digite um número inteiro.")
                        print('\n')



            while True:
                    try:
                        idade = int(input("Digite a sua idade : "))
                        print('\n')
                        break
                    except ValueError:
                        print("Idade inválida. Digite um número inteiro.")
                        print('\n')
            
            email = input("Digite o seu email : ")


            animais_disponiveis = [
                "Cachorro",
                "Gato",
                "Coelho",
                "Pássaro",
                "Peixe",
                "Hamster",
                "Porquinho-da-Índia",
                "Tartaruga"
            ]

            # Exibir animais disponíveis para escolha
            print("Animais disponíveis:")
            for i, animal in enumerate(animais_disponiveis, start=1):
                print(f"{i}. {animal}")

            escolha_animal = input("Digite o número do animal de sua preferência: ")
            escolha_animal = int(escolha_animal)

            if escolha_animal < 1 or escolha_animal > len(animais_disponiveis):
                print("Escolha inválida.")
                return

            animal_escolhido = animais_disponiveis[escolha_animal - 1]

            while True:
                    cor = input("Digite a cor do animal de sua preferência:  ")
                    print('\n')
                    if not cor.replace(" ", "").isalpha(): 
                        print("cor inválida. Digite apenas letras.")
                        print("\n")
                    else:
                        break

            idade_animal = input("Digite a idade do animal de sua preferência  ")


            particularidade = input("Digite a particularidade do animal de sua preferência ou s/n para nenhuma particlaridade: ")

            self.cur.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?, ?, ?,?)",
                            (nome, idade, email, animal_escolhido, cor, idade_animal, particularidade,cpf))
            self.con.commit()
            self.con.close()
            print("Cadastro de pessoas realizado com sucesso!")
        except sqlite3.Error as e:
            print(f"Ocorreu um erro ao cadastrar a pessoa: {str(e)}")




   