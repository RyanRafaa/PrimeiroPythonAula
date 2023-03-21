import os

# nome = "Ryan "
os.system("cls ") #limpa terminal
# for letra in nome:
#     print(letra)

# carros = ("Civic", "Corolla", "Cruze")

# print(type(carros))

# for tuplas in carros:
#     print(tuplas)
#     print("_________________________")

# lista1 = ["Informática", "Medicina", "Engenharia"]

# print(type(lista1))

# lista1.append("Biomedicina")#Para inserir um valor

# lista1.remove("Medicina")#Para remover um valor

# for listageral in lista1:
#     print (listageral)


    # Inserir, Editar, Apagar, Consultar

print("Lista de Compras")

# print (listacompras)
# print ("_______________________________________")
# print("Selecione a ação desejada:")
# opcao = str(input("[i]Inserir,  [e]Editar,  [c]Consultar,  [a]Apagar: "))
# print ("_______________________________________")
listacompras = []

while True:
    print("Selecione a ação desejada:")
    opcao = input("[i]Inserir,  [e]Editar,  [c]Consultar,  [a]Apagar,   [s]Sair: ")
    print ("_______________________________________")
    if opcao == "i" or opcao == "inserir" or opcao == "Inserir":
        inserindo = input("Digite o item que deseja inserir: ")
        listacompras.append(inserindo)
        
        os.system("cls ")
        print (f"{inserindo} inserido com sucesso")
        print ("_______________________________________")
    elif opcao == "c" or opcao == "consultar" or opcao == "Consultar":
        os.system("cls ")
        print (f"sua lista de compras atual é {listacompras}")
        print ("_______________________________________")    
    elif opcao == "a" or opcao == "apagar" or opcao == "Apagar":
        print (f"sua lista de compras atual é {listacompras}")
        apagando = (input("Digite o item que deseja apagar: "))
        
        if apagando != listacompras:
            print("Não existe esse item na sua lista")
        else:
            listacompras.remove(apagando)
    elif opcao == "e" or opcao == "editar" or opcao == "Editar":
        print (f"sua lista de compras atual é {listacompras}")
        editando = (input("Digite o item que deseja editar: "))
        if editando in listacompras:
            listacompras.remove(editando)
            novovalor = (input("Digite o novo item: "))
            listacompras.append(novovalor)
            print (f"{editando} foi substituido por {novovalor}")   
        else:
            print("Não existe esse item na sua lista")        
    elif opcao == "s" or opcao == "sair" or opcao == "Sair":
        print("sistema finalizado!")
        break




