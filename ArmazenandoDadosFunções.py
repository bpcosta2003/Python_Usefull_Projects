def escolher():

    escolha = input(
        "\nO que deseja realizar ? \n\n"
        "<I> Para Inserir usuário\n"
        "<P> Para Pesquisar usuário\n"
        "<E> Para Excluir usuário\n"
        "<L> Para Listar usuário\n"
        "<S> Para Sair\n\n"
    ).upper()

    return escolha


def inserir(dicionario):

    chave = input("Digite o seu login : ").upper()

    dicionario[chave] = [
        input("Digite o seu nome : ").upper(),
        input("Digite a sua última data de acesso : "),
        input("Qual a sua última estação acessada : ").upper()
    ]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome.........................:" + lista[0])
        print("Última data de acesso........:" + lista[1])
        print("Última estação acessada......:" + lista[2])
    else:
        print('USUÁRIO NÃO ENCONTRADO')


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Usuário excluído")
    else:
        print('USUÁRIO NÃO ENCONTRADO')


def listar(dicionario, chave):
    for chave, valor in dicionario.items():
        print("Objeto..........")
        print(f'Login : {chave}')
        print(f'Dados : {valor}')


def sair():
    exit()
