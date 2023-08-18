class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


autor1 = Autor("João da Silva", "01/01/1980")


livro1 = Livro("Aventuras na Floresta", autor1)
livro2 = Livro("Segredos do Universo", autor1)


print("Livro 1:")
print(f"Título: {livro1.titulo}")
print(f"Autor: {livro1.autor.nome}")
print(f"Data de Nascimento do Autor: {livro1.autor.data_nascimento}")
print("\nLivro 2:")
print(f"Título: {livro2.titulo}")
print(f"Autor: {livro2.autor.nome}")
print(f"Data de Nascimento do Autor: {livro2.autor.data_nascimento}")
