from teste import Pessoa

class Programador(Pessoa):
    def __init__(self, nome, linguagem):
        super().__init__(nome)
        self.linguagem = linguagem
        print(f"programador {self.nome}, linguagem: {self.linguagem}")


maria = Programador("Maria", "Python")