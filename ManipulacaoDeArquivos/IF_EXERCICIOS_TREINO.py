from operator import itemgetter


# / 1

bpm = int(input("Qual seu número de batimentos por minuto : "))
idade = int(input("Qual a sua idade : "))

if idade >= 0 and idade < 3 and bpm >= 120 and bpm <= 140:
    print("Seu BPM está NORMAL")
elif idade >= 0 and idade < 3 and bpm < 120:
    print("Seu BPM etá ABAIXO DO NORMAL")
elif idade >= 0 and idade < 3 and bpm > 140:
    print("Seu BPM está ACIMA DO NORMAL")

elif idade >= 8 and idade < 18 and bpm >= 80 and bpm <= 100:
    print("Seu BPM está NORMAL")
elif idade >= 8 and idade < 18 and bpm < 80:
    print("Seu BPM etá ABAIXO DO NORMAL")
elif idade >= 8 and idade < 18 and bpm > 100:
    print("Seu BPM está ACIMA DO NORMAL")

elif idade >= 18 and idade < 65 and bpm >= 70 and bpm <= 80:
    print("Seu BPM está NORMAL")
elif idade >= 18 and idade < 65 and bpm < 70:
    print("Seu BPM etá ABAIXO DO NORMAL")
elif idade >= 18 and idade < 65 and bpm > 80:
    print("Seu BPM está ACIMA DO NORMAL")

elif idade >= 65 and bpm >= 50 and bpm <= 60:
    print("Seu BPM está NORMAL")
elif idade >= 65 and bpm < 50:
    print("Seu BPM etá ABAIXO DO NORMAL")
elif idade >= 65 and bpm > 60:
    print("Seu BPM está ACIMA DO NORMAL")

# / 2

valor_bruto = float(input("\nDigite o valor bruto do pacote : "))

loop = True

while loop == True:

    categoria_assentos = int(input(
        "Qual a categoria dos assentos : \n< 1 > economica\n< 2 > executiva\n< 3 > primeira classe\n: "))

    if categoria_assentos == 1:
        viajantes = int(input("Qual a quantidade de viajantes : "))
        if viajantes == 2:
            d = 0.03
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        elif viajantes == 3:
            d = 0.04
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        elif viajantes >= 4:
            d = 0.05
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        loop = False

    elif categoria_assentos == 2:
        viajantes = int(input("Qual a quantidade de viajantes : "))
        if viajantes == 2:
            d = 0.05
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        elif viajantes == 3:
            d = 0.07
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        elif viajantes >= 4:
            d = 0.08
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        loop = False

    elif categoria_assentos == 3:
        viajantes = int(input("Qual a quantidade de viajantes : "))
        if viajantes == 2:
            d = 0.10
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        elif viajantes == 3:
            d = 0.15
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        elif viajantes >= 4:
            d = 0.20
            valor_bruto_desconto = valor_bruto * d
            print(
                f'O valor caiu de {valor_bruto} para {valor_bruto - valor_bruto_desconto} pois houve um desconto de {d} e o valor médio por viajante é de {(valor_bruto - valor_bruto_desconto) / viajantes:.2f}')
        loop = False
    else:
        print("Opção Inválida")
        loop = True


# / 3

ps5 = []
xbox = []
nintendo = []

console = {
    'PS5': ps5,
    'XBOX': xbox,
    'NINTENDO': nintendo
}

for i in range(1, 6):
    votos = int(input(
        "Qual console quer votar :\n< 1 > Para o PS5\n< 2 > Para o XBOX\n< 3 > Para o NINTENDO\n:"))

    while votos < 1 and votos > 3:
        print("Opção Inválida")
        votos = int(input(
            "Qual console quer votar :\n< 1 > Para o PS5\n< 2 > Para o XBOX\n< 3 > Para o NINTENDO\n:"))

    if votos == 1:
        ps5.append(1)

    elif votos == 2:
        xbox.append(1)

    elif votos == 3:
        nintendo.append(1)

ranking = []

ranking = sorted(console.items(), key=itemgetter(1), reverse=True)

print(
    f'O console escolhido foi o {ranking[0][0]} com {sum(ranking[0][1])} votos.')
