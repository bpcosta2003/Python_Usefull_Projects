from operator import itemgetter
'''
# / 1

soma_par = []
soma_impar = []

print('\n--------------------------------')

print("\nPARTE IMPAR DA SALA :\n")

print('--------------------------------\n')

for j in range(1, 51, 2):
    nota = float(input(f'\nDigite a nota do {j}.o aluno : '))
    soma_impar.append(nota)

print('\n--------------------------------')

print('\nPARTE PAR DA SALA :\n')

print('--------------------------------\n')

for i in range(1, 51):
    if i % 2 == 0:
        nota = float(input(f'\nDigite a nota do {i}.o aluno : '))
        soma_par.append(nota)

media_impar = (sum(soma_impar)) / 25

media_par = (sum(soma_par)) / 25

maior_media = {
    'SALA PAR': media_par,
    'SALA ÍMPAR': media_impar
}

print('\n--------------------------------')

for k, v in maior_media.items():
    print(f'\nA {k} teve a média de {v}\n')

print('\n--------------------------------')

ranking = sorted(maior_media.items(), key=itemgetter(1), reverse=True)


print(f'\nA {ranking[0][0]} teve a média mais alta com {ranking[0][1]}')
'''
# / 2

minutos = int(input("Informe os minutos atuais : "))

factorial = 1

for i in range(1, minutos+1):
    factorial = factorial * i

print(f'A senha é : LIBERDADE{factorial}')
