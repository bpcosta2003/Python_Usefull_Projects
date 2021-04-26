from ArmazenandoDadosFunções import *

usuarios = {}

opc = escolher()

while opc == 'I' or opc == 'P' or opc == 'E' or opc == 'L' or opc == 'S':

    if opc == 'I':
        inserir(usuarios)

        pergunta = input(
            "Voce quer realizar outra função ? ('S' para sim 'N' para não) ").upper()
        if pergunta == 'S':
            opc = escolher()
        elif pergunta == 'N':
            exit()
        else:
            opc = escolher()
            print(opc)

    # /Só vai exibir as pesquisas e eliminações e listas de usuários se colocar em maiúsculo o login

    elif opc == 'P':
        pesquisar(usuarios, input("Qual login deseja pesquisar : "))
        pergunta = input(
            "Voce quer realizar outra função ? ('S' para sim 'N' para não) ").upper()
        if pergunta == 'S':
            opc = escolher()
        elif pergunta == 'N':
            exit()
        else:
            opc = escolher()
            print(opc)

    elif opc == 'E':
        excluir(usuarios, input("Qual login deseja excluir : "))
        pergunta = input(
            "Voce quer realizar outra função ? ('S' para sim 'N' para não) ").upper()
        if pergunta == 'S':
            opc = escolher()
        elif pergunta == 'N':
            exit()
        else:
            opc = escolher()
            print(opc)

    elif opc == 'L':
        listar(usuarios)
        pergunta = input(
            "Voce quer realizar outra função ? ('S' para sim 'N' para não) ").upper()
        if pergunta == 'S':
            opc = escolher()
        elif pergunta == 'N':
            exit()
        else:
            opc = escolher()
            print(opc)

    elif opc == 'S':
        sair()
