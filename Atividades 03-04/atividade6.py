# Desenvolva um dicionário em Python para armazenar o nome e a nota de 3 alunos, realizando a leitura dos valores por meio de um estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retorne a média.

alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

somaNotas = 0
for nota in alunos.values():
    somaNotas += nota

media = somaNotas / len(alunos)

print(f"Média das notas dos alunos: {media}")