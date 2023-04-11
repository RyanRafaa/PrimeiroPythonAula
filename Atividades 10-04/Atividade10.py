def media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [25, 13, 58, 41, 12]
resultado = media(numeros)
print("A média dos números é:", resultado)