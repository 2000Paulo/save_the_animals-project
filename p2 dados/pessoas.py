from animais import *
import sqlite3
class Cadastro_pessoas:
    def __init__(self):
        self.con = sqlite3.connect('banco_de_dados.db')
        self.cur = self.con.cursor()

    def cadastro(self):
        try:
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade da pessoa: ")
            email = input("Digite o email da pessoa: ")

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

            escolha_animal = input("Digite o número do animal de preferência da pessoa: ")
            escolha_animal = int(escolha_animal)

            if escolha_animal < 1 or escolha_animal > len(animais_disponiveis):
                print("Escolha inválida.")
                return

            animal_escolhido = animais_disponiveis[escolha_animal - 1]

            cor = input("Digite a cor do animal de preferência da pessoa: ")
            idade_animal = input("Digite a idade do animal de preferência da pessoa: ")
            particularidade = input("Digite a particularidade do animal de preferência da pessoa: ")

            self.cur.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (nome, idade, email, animal_escolhido, cor, idade_animal, particularidade))
            self.con.commit()
            self.con.close()
            print("Cadastro de pessoas realizado com sucesso!")
        except sqlite3.Error as e:
            print(f"Ocorreu um erro ao cadastrar a pessoa: {str(e)}")
