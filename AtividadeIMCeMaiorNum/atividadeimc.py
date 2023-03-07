nome = input('Qual o seu nome? ')
peso = float (input("Qual o seu peso em Quilogramas? (ex 60) "))
altura = float (input("Qual a sua altura Metros? (ex: 1.80) "))

calc1 = peso/(altura*altura)

if calc1 < 18.5:
    print ("Olá ",nome," seu é IMC é de Abaixo do peso")
elif calc1 >= 18.5 and calc1 <= 24.9:
    print ("Olá ",nome," seu é IMC é de Peso normal")
elif calc1 >= 25.0 and calc1 <= 29.9:
    print ("Olá ",nome," seu é IMC é de Pré-obesidade")
elif calc1 >= 30.0 and calc1 <= 34.9:
    print ("Olá ",nome," seu é IMC é de Obesidade Grau 1")
elif calc1 >= 35.0 and calc1 <= 39.9:
    print ("Olá ",nome," seu é IMC é de Obesidade Grau 2")
elif calc1 > 40:
    print ("Olá ",nome," seu é IMC é de Obesidade Grau 3")
