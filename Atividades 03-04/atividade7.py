# Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somas todos os elementos da matriz

# dieimes_matriz = np.array ([[3,4,1], [3,1,2]])


import numpy as np

dieimes_matriz = np.array([[3, 4, 1], [3, 1, 2]])

soma = 0

for linha in dieimes_matriz:
    for elemento in linha:
        soma += elemento

print("A soma de todos os elementos da matriz é:", soma)