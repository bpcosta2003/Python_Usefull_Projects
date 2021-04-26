
# * função de cadastro de informações

def cadastrar(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [
            input("Digite seu nome : "),
            input("Digite o equipamento : "),
            float(input("Digite o valor : ")),
            int(input("Digite o número serial: ")),
            input("Digite o departamento : ")
        ]

        lista.append(equipamento)

        resposta = input("Digite 'S' para continuar e 'N' para sair: ").upper()


# * função exibição de informações x1

def exibir(lista):
    for elemento in lista:
        print(" - - - - ")
        print("Informações...", lista.index(elemento))
        print(" - - - - ")
        print("Seu nome :", elemento[0])
        print("Equipamento :", elemento[1])
        print("Valor :", elemento[2])
        print("Serial :", elemento[3])
        print("Departamento :", elemento[4])
        print(" - - - - ")


# * função de busca de equipamentos

def buscar(lista):
    print(" - - - - ")
    busca = input("Digite o nome do equipamento que deseja buscar : ")
    print(" - - - - ")

    for elemento in lista:
        if busca == elemento[1]:
            print(" - - - - ")
            print(f'Informações do(a) {busca} :')
            print(f'A pessoa que cadastrou foi = {elemento[0]}')
            print(f'Valor = {elemento[2]}')
            print(f'Serial = {elemento[3]}')
            print(f'Departamento = {elemento[4]}')
            print(" - - - - ")


# * função de depreciação de equipamentos

def depreciar(lista):
    depreciação = input("Digite o equipamento que sofrerá uma deprecição : ")
    porcentagem = int(input("Informe a porcentagem para depreciação : "))
    for elemento in lista:
        if elemento[1] == depreciação:
            print(" - - - - ")
            print(
                f'O valor do(a) {depreciação} sofreu uma depreciação de {porcentagem}%')
            print(
                f'O valor do(a) {depreciação} era : {elemento[2]} e agora é : {elemento[2] * (1-porcentagem/100)}')
            print(" - - - - ")

# * função de eliminação do serial de equipamentos


def eliminar(lista):
    serial = int(
        input("Digite o numero serial do equipamento que será excluído : "))

    for elemento in lista:
        if elemento[3] == serial:
            print(" - - - - ")
            print(
                f'O equipamento com o numero serial {serial} será excluído pois foi danificado')
            lista.remove(elemento)
            return "Itens excluídos"
            print(" - - - - ")

# * função exibição de informações x2


# * função de comparação de valores

def comparar(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[2])
        if len(valores) > 0:
            print(f'O equipamento mais caro custa : {max(valores)}')
            print(f'O equipamento mais barato custa : {min(valores)}')
            print(f'A soma dos equipamentos é de : {sum(valores)}')
