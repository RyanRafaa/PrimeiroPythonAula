sistema = True

while sistema:
    nome = input ("Escreva o seu nome: ")
    print (f"O nome recebido foi: {nome}")

    if nome == "sair":
        print ("Finalizou o sistema!")
        break

contador = 0

while contador <= 100:
    print(contador)
    contador = contador +1

    if contador == 24:
        print ("Lá eleeeee")
        continue
    elif contador == 69:
        print ("Sexooo")
        continue
print ("Mas é só a musga")        

tabuada = int(input("qual a tabuada que você deseja? "))
quantidade = 1

while quantidade <= 10:
    
    print (f"{quantidade} X {tabuada} = {quantidade * tabuada}")
    quantidade += 1


while True:
    numero1 = input("Escreva o primeiro número: ")
    

    operador = input("Digite o operador (+-*/%) ")

    numero2 = input("Escreva o segundo número: ")
    

    
    
    if operador == "+":
        print(f"Resultado: {numero1 + numero2}")
    elif operador == "-":
        print(f"Resultado: {numero1 - numero2}") 
    elif operador == "*" or "x" or "X":
        print(f"Resultado: {numero1 * numero2}") 
    elif operador == "/":
        print(f"Resultado: {numero1 / numero2}")  
    elif operador == "%":
        print(f"Resultado: {numero1 / numero2}")
    else:
        print("Operador inválido")             

    sair = input("Deseja sair? ").lower().startswith("s")
    if sair:
        break

