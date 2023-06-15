import sqlite3
import random

class Relatorio:
    def __init__(self):
        self.con = sqlite3.connect('banco_de_dados.db')
        self.cur = self.con.cursor()

    def gerar_relatorio(self):
        self.cur.execute("""
            SELECT nome, especie, cor, idade_animal
            FROM pessoas
        """)

        pessoas = self.cur.fetchall()

        for pessoa in pessoas:
            nome, especie, cor, idade_animal = pessoa

            self.cur.execute("""
                SELECT id, especie, idade_animal, cor, porte, particularidade
                FROM animais
                WHERE especie = ? AND cor = ? AND idade_animal = ?
            """, (especie, cor, idade_animal))

            animais_compativeis = self.cur.fetchall()

            print(f"Perfil da pessoa: {nome}")
            print("------------------------------")
            print("Animais compatíveis:")
            if animais_compativeis:
                for animal in animais_compativeis:
                    id_animal, especie, idade_animal, cor, porte, particularidade = animal
                    print(f"Número: {id_animal}")
                    print(f"Espécie: {especie}")
                    print(f"Idade: {idade_animal}")
                    print(f"Cor: {cor}")
                    print(f"Porte: {porte}")
                    print(f"Particularidade: {particularidade}")
                    print("------------------------------")
            else:
                print(f"Não foram encontrados animais compatíveis com o perfil do(a) {nome}.")
            print("\n")

    def pesquisar_pessoa(self, cpf_pessoa):
        self.cur.execute("""
            SELECT nome, especie, cor, idade_animal
            FROM pessoas
            WHERE cpf = ?
        """, (cpf_pessoa,))

        pessoa = self.cur.fetchone()

        if pessoa:
            nome, especie, cor, idade_animal = pessoa

            self.cur.execute("""
                SELECT id, especie, idade_animal, cor, porte, particularidade
                FROM animais
                WHERE especie = ? AND cor = ? AND idade_animal = ?
            """, (especie, cor, idade_animal))

            animais_compativeis = self.cur.fetchall()

            print(f"Informações da pessoa: {nome}")
            print("------------------------------")
            print("Animais compatíveis:")
            if animais_compativeis:
                for numero, animal in enumerate(animais_compativeis, start=1):
                    id_animal, especie, idade_animal, cor, porte, particularidade = animal
                    print(f"Número: {numero}")
                    print(f"Espécie: {especie}")
                    print(f"Idade: {idade_animal}")
                    print(f"Cor: {cor}")
                    print(f"Porte: {porte}")
                    print(f"Particularidade: {particularidade}")
                    print("------------------------------")
            else:
                print(f"Não foram encontrados animais compatíveis com o perfil da pessoa.")
            print("\n")
        else:
            print("Pessoa não encontrada.")

    def adotar_animal(self, id_animal, nome_pessoa):
        self.cur.execute("""
            DELETE FROM animais
            WHERE id = ?
        """, (id_animal,))

        self.con.commit()
        print(f"Parabéns, {nome_pessoa}! Você acaba de adotar um animal.")
        print("\n")

    def listar_animais(self):
        self.cur.execute("SELECT * FROM animais")
        animais = self.cur.fetchall()

        for animal in animais:
            especie, idade_animal, cor, porte, particularidade, id_animal, descricao = animal
            print("Espécie:", especie)
            print("Idade do Animal:", idade_animal)
            print("Cor:", cor)
            print("Porte:", porte)
            print("Particularidade:", particularidade)
            print("ID:", id_animal)
            print("Descrição:", descricao)
            print("---------------------------")

    def fechar_conexao(self):
        self.con.close()
