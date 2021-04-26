from BuscaDeValoresFunções import *

minhalista = []

cadastrar(minhalista)
exibir(minhalista)

pergunta1 = input(
    "Você quer buscar um item ? (DIGITE 'S' PARA SIM E 'N' PARA NÃO) : ").upper()
if pergunta1 == 'S':
    buscar(minhalista)
else:
    pass

pergunta2 = input(
    "Você quer depreciar um item ? (DIGITE 'S' PARA SIM E 'N' PARA NÃO) : ").upper()
if pergunta2 == 'S':
    depreciar(minhalista)
else:
    pass

pergunta3 = input(
    "Você quer excluir um item ? (DIGITE 'S' PARA SIM E 'N' PARA NÃO) : ").upper()
if pergunta3 == 'S':
    eliminar(minhalista)
else:
    pass

exibir(minhalista)
comparar(minhalista)
