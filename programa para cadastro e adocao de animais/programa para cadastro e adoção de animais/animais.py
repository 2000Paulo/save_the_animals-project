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

        border_horizontal = "═" * 34  
        print("╔" + border_horizontal + "╗")  
        for i, animal in enumerate(animais, start=1):
            print("║ " + f"{i}. {animal:<30}" + "║")  
        print("╚" + border_horizontal + "╝")  
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
                        print('\n')
                        break
                    except ValueError:
                        print("Idade inválida. Digite um número inteiro.")
                        print('\n')

                while True:
                    cor = input("Digite a cor desejada para o animal: ")
                    print('\n')
                    if not cor.isalpha():
                        print("Cor inválida. Digite apenas letras.")
                        print('\n')
                    else:
                        break

                while True:
                    porte = input("Digite o porte do animal (1 para pequeno, 2 para médio, 3 para grande): ")
                    print('\n')
                    if porte not in ['1', '2', '3']:
                        print("Porte inválido. Digite apenas 1 para pequeno, 2 para médio ou 3 para grande.")
                        print('\n')
                    else:
                        if porte == '1':
                            porte = 'pequeno'
                        elif porte == '2':
                            porte = 'médio'
                        else:
                            porte = 'grande'
                        break

                while True:
                    particularidade = input("Digite alguma particularidade do animal ou s/n para nenhuma : ")
                    if not particularidade.strip():
                        print("Este campo não pode ficar vazio!")
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

    
