from random import randint
from time import sleep
from operator import itemgetter


#!Desafio 1

aluno = dict()
aluno['Nome'] = input("Nome : ")
aluno['Media'] = float(input(f'Media do {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] >= 5 and aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

#!Desafio 2

jogo = {
    'jogador_1': randint(1, 6),
    'jogador_2': randint(1, 6),
    'jogador_3': randint(1, 6),
    'jogador_4': randint(1, 6)
}

ranking = list()

print(f'Valores sorteados :')

for k, v in jogo.items():
    print(f'O {k} jogou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f' ')
print("------------------------------------------------")
print("                   RANKING")
print("------------------------------------------------")

for i, v in enumerate(ranking):

    print(f'\n{i+1}.o lugar : {v[0]} com {v[1]} no dado')
    sleep(1)

#!Desafio 3

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input("Qual o nome do jogador : ")
    total = int(input(f'Quantas partidas o {jogador["nome"]} jogou : '))
    partidas.clear()

    for num in range(0, total):
        partidas.append(
            int(input(f'Quantos gols o {jogador["nome"]} fez na partida {num+1} : ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input("Quer continuar : [S/N] ").upper()[0]
        if resp in 'SN':
            break
        else:
            print("ERRO VOCE DEVE ESCREVER S OU N ")
    if resp == 'N':
        break

print("----------------------------------------------------------------")

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('----------------------------------------------------------------')

for k, v in enumerate(time):
    print(f'{k:>3} ', end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()

print("----------------------------------------------------------------")

while True:
    busca = int(input("Mostrar dados de qual jogador (999 para parar) : "))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO JOGADOR {busca} NÃO ENCONTRADO !')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} : ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols')

    print("----------------------------------------------------------------")
