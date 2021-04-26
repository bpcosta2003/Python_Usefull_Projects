from ManipulaçaoDeArquivosFunções import *

inventario = {}

opcao = chamarMenu()

while opcao > 0 and opcao < 4:

    if opcao == 1:
        registrar(inventario)

    elif opcao == 2:
        persistir(inventario)

    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data............", lista[1])
            print("Descrição.......", lista[2])
            print("Departamento....", lista[3])

    opcao = chamarMenu()
