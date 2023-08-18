# 1
def saudacao():
    print("Olá! Bem-vindo ao meu programa.")


saudacao()

# 2
def verificar_paridade(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")


verificar_paridade(10)
verificar_paridade(7)
verificar_paridade(22)

#3
def calcular_area_retangulo(comprimento, largura):
    area = comprimento * largura
    return area


area1 = calcular_area_retangulo(5, 8)
area2 = calcular_area_retangulo(10, 3)
area3 = calcular_area_retangulo(7, 7)

print(f"A área do primeiro retângulo é: {area1}")
print(f"A área do segundo retângulo é: {area2}")
print(f"A área do terceiro retângulo é: {area3}")


