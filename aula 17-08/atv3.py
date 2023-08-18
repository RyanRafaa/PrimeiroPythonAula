class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor


motor1 = Motor("Gasolina", 150)


carro1 = Carro(motor1)


print("Carro:")
print(f"Tipo de Motor: {carro1.motor.tipo}")
print(f"Potência do Motor: {carro1.motor.potencia} cavalos")
