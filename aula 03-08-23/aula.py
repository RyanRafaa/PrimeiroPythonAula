import os
lista = []
os.system("cls")
while True:
    print("Selecione a Opção")
    opcao = input ("[i}nserir [a]pagar [l]istar [e]ditar [s]sair")
    if opcao == "i":
        os.system("cls")
        valor = input("Digite o Valor: ")
        lista.append(valor)
        print ("Valor inserido com Sucesso")
        print ("__________________________")
    elif opcao == "a":
        os.system("cls")
        apagar = input ("Qual valor deseja apagar: ")

        try:
            lista.remove(apagar)
            print ("Valor apagado com Sucesso")
            print ("__________________________")
        except ValueError:
            print ("Valor não encontrado")
            print ("__________________________")
    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")
            print ("__________________________")
        else:
            for i, listageral in enumerate (lista):
                print ("__________________________")
                print (i, listageral)
            print ("__________________________")
    elif opcao == "e":
        os.system("cls")
        editar = input ("Qual valor deseja editar: ")
        novovalor = input ("Qual valor deseja colocar: ")

        try:
            lista.remove(editar)
            lista.append(novovalor)
            print ("Valor editado com Sucesso")
            print ("__________________________")
        except ValueError:
            print ("Valor não encontrado")
            print ("__________________________")
    elif opcao == "s":
        os.system("cls")
        print ("Sessão encerrada")
        print ("__________________________")
        break

