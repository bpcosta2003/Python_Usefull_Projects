
# !Desafio 1 -
# *Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console

with open("Inscritos.txt", "r") as arq:
    for inscrito in arq:
        print(inscrito)

# !Desafio 2 -
# *Adicione o seu nome na lista de inscritos e depois todos os nomes que estão no arquivo inscritos.txt no console

with open("Inscritos.txt", "a") as arq:
    arq.write("Bruno de Paula Costa\n")


# !Desafio 3 -
# *Com o seu nome já na lista de inscritos, exiba o nome de cada pessoas que está inscrito na lista + o número que ele representa na lista em ordem crescente (ex: 1 jhonatan , 2 Patricio Silva, 3 Kid Boy 3000)

with open("Inscritos.txt", "r") as arq:
    cont = 0
    for inscrito in arq:
        cont = cont + 1
        print(cont, inscrito)
