import os
os.system("cls ") #limpa terminal


def temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura

def fahrenheit(tempCelsius):
    tempFahrenheit = (9 * tempCelsius + 160) / 5
    return tempFahrenheit

def resultado(tempFahrenheit):
    print(f"A temperatura em graus Fahrenheit é de {tempFahrenheit}F°")

tempCelsius = temperatura()
tempFahrenheit = fahrenheit(tempCelsius)
resultado(tempFahrenheit)
