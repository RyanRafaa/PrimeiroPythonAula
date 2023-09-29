class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        

class Presencial(Curso):
    def __init__(self, numero_de_vagas):
        super().__init__(Curso)
        self.numero_de_vagas = numero_de_vagas


class Online(Curso):
    def __init__(self, plataforma_online):
        super().__init__(Curso)
        self.plataforma_online = plataforma_online´


class detalhes
    return f"O curso {super().detalhes()}"       
        print(f"programador {self.nome}, linguagem: {self.linguagem}")


maria = Programador("Maria", "Python")





