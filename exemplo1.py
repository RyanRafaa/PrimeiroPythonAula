import os
os.system('cls')


# def exemplo(a,b,c):
#     print(a,b,c)

# exemplo(1,2,3)
# exemplo(a=1,b=2,c=3)

# def minha_funcao (*args):
#     for arg in args:
#         print(arg)
#     print(type(args))

# minha_funcao(1,2,3,'oi')

# def minha_funcao (**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"A chave é {chave} e o valor é {valor}")
#     print(type(kwargs))

# minha_funcao(nome='João', idade=25, país="Brasil")

def minha_funcao ():
    return "Função do módulo!"

if __name__ == '__main__':
    print("Este script está sendo executado sozinho!")
else:
    print("Este script foi importado!")
