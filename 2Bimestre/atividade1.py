class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

    def imprimir_saldo(self):
        print(f"Saldo da conta {self.numero_conta} do titular {self.nome_titular}: R$ {self.saldo:.2f}")


minha_conta = ContaBancaria(1111, "Ryan Rafael", 300)
minha_conta.imprimir_saldo()

minha_conta.depositar(600)
minha_conta.imprimir_saldo()

minha_conta.sacar(300.0)
minha_conta.imprimir_saldo()

minha_conta.sacar(1200.0)
minha_conta.imprimir_saldo()