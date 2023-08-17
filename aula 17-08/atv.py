class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

    def mostrar_so(self):
        return f"{self.nome}, {self.versao}"

class Computador:
    def __init__(self, nome, so):
        self.nome = nome
        self.so = so

    def mostrar_informacoes(self):
        return f"{self.nome} tem o sistema operacional {self.so.mostrar_so()}"

pc_linux = SistemaOperacional ("linux", "kali")
dell = Computador ("dell", pc_linux)

print (dell.mostrar_informacoes())