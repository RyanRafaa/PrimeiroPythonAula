# Crie um script em Python e utilize o FOR para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar os valores digitados.

listaNumeros = []

for i in range(5):
    valores = int(input("Digite um número inteiro: "))
    listaNumeros.append(valores)

soma = 0


for valores in listaNumeros:
    soma += valores

print("A soma dos números digitados é:", soma)