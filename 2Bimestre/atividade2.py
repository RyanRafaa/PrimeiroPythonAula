class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores

    def adiciona_jogador(self, nome, camisa):
        self.jogadores.append([nome, camisa])

    def imprime_jogadores(self):
        print(f"Lista de jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(f" - {jogador[1]} - {jogador[0]}")

jogadores = [["Ryan", 11], ["Lucas", 10], ["William", 1]]
meu_time = Time("Time do Noel", jogadores)
meu_time.imprime_jogadores()

meu_time.adiciona_jogador("Caio", 9)
meu_time.imprime_jogadores()