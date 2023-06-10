import sqlite3

class CadastroAnimais:
    def __init__(self):
        self.con = sqlite3.connect('banco_de_dados.db')
        self.cur = self.con.cursor()

    def exibir_animais_adotados(self):
        animais = [
            "Cachorro",
            "Gato",
            "Coelho",
            "Pássaro",
            "Peixe",
            "Hamster",
            "Porquinho-da-Índia",
            "Tartaruga",
            
        ]

        border_horizontal = "═" * 34  # Caractere utilizado para formar a linha horizontal
        print("╔" + border_horizontal + "╗")  # Canto superior esquerdo da caixa
        for i, animal in enumerate(animais, start=1):
            print("║ " + f"{i}. {animal:<30}" + "║")  # Conteúdo da caixa alinhado à esquerda
        print("╚" + border_horizontal + "╝")  # Canto inferior esquerdo da caixa
    def cadastrar_animal(self):
        while True:
        # Exibindo a lista de animais disponíveis
            self.exibir_animais_adotados()

        # Solicitando a escolha do animal pelo número
            numero = input("Escolha o número do animal desejado: ")

            try:
                numero = int(numero)
                if numero < 1 or numero > 10:
                    raise ValueError

            # Recuperando o nome do animal selecionado
                animais = [
                "Cachorro",
                "Gato",
                "Coelho",
                "Pássaro",
                "Peixe",
                "Hamster",
                "Porquinho-da-Índia",
                "Tartaruga"
                ]
                animal_escolhido = animais[numero - 1]

            # Solicitando as informações adicionais
                while True:
                    try:
                        idade = int(input("Digite a idade do animal: "))
                        break
                    except ValueError:
                        print("Idade inválida. Digite um número inteiro.")

                while True:
                    cor = input("Digite a cor desejada para o animal: ")
                    if not cor.isalpha():
                        print("Cor inválida. Digite apenas letras.")
                    else:
                        break

                while True:
                    porte = input("Digite o porte do animal: ")
                    if not porte.isalpha():
                        print("Porte inválido. Digite apenas letras.")
                    else:
                        break

                while True:
                    particularidade = input("Digite alguma particularidade do animal: ")
                    if not particularidade.isalpha():
                        print("Particularidade inválida. Digite apenas letras.")
                    else:
                        break

                while True:
                    descricao = input("Faça uma breve descrição do animal, com informações relevantes: ")
                    if descricao.strip():
                            break
                    else:
                            print("Este campo não pode ficar vazio!")

            # Inserindo o animal escolhido na tabela "animais"
                self.cur.execute("INSERT INTO animais (especie, idade_animal, cor, porte, particularidade, descricao) "
                             "VALUES (?, ?, ?, ?, ?, ?)",
                             (animal_escolhido, idade, cor, porte, particularidade, descricao))
                self.con.commit()

            # Recuperando o ID do animal cadastrado
                animal_id = self.cur.lastrowid
                print(f"Número do animal no banco de dados: {animal_id}")

                self.con.close()
                print(f"Animal '{animal_escolhido}' cadastrado com sucesso!")
                break
            except ValueError:
                print("Número inválido. Tente novamente.")

    
