from geopy.geocoders import Nominatim
import json
import os


def chamarMenu():
    escolha = escolha = int(input(
        "Digite:\n< 1 > para registrar endereço\n< 2 > para exibir informações do endereço: \n< 3 > para achar endereço pelas coordenadas\n"))
    return escolha


def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario


def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)


def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":

        dicionario[input("Digite o cep: ")] = [
            input("Digite a rua: "),
            input("Digite o numero: "),
            input("Digite o bairro: "), input("Digite a cidade: "), input("Digite o estado: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario, arquivo)
        break
    return "JSON gerado!!!!"


def exibir(dicionario, arquivo):
    dicionario = ler_arquivo(arquivo)
    endereço = open("entrada_json.json")
    print(endereço.readlines(1))
