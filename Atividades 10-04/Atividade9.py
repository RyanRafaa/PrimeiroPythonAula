import os
os.system("cls ") #limpa terminal

def tipo():
    tipo = float(input("Digite o valor em R$ do litro do combustível do seu carro: "))
    return tipo

def litros():
    litros = float(input("Digite a média de litros por KM que seu veículo gasta: "))
    return litros

def tempo():
    tempo = float(input("Digite o tempo médio em horas que será gasto para realizar a viagem: "))
    return tempo

def velocidade():
    velocidade = float(input("Digite a velocidade média em KM/h do veículo durante a viagem: "))
    return velocidade

def distancia(velocidade, tempo):
    distancia = (tempo * velocidade)
    return distancia

def gasolina(distancia, litros):
    gasolina = (distancia / litros)
    return gasolina

def gastos(gasolina, tipo):
    gastos = (gasolina * tipo)
    return gastos

def resultado(gasolina, gastos):
    resultado = gasolina
    print("-" * 40)
    print(f"A quantidade de litros de combustível gastos nessa viagem é de {gasolina: .2f} por KM")
    print(f"O valor gasto em combustível será de R${gastos: .2f}")
    print("-" * 40)
    return resultado



tipo = tipo()
litros = litros()
tempo = tempo()
velocidade = velocidade()
distancia = distancia(velocidade, tempo)
gasolina = gasolina(distancia, litros)
gastos = gastos(gasolina, tipo)
resultado(gasolina, gastos)

