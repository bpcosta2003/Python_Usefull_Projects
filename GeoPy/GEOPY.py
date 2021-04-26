from geopy.geocoders import Nominatim
from GEOPYfuncoes import *
geolocator = Nominatim(user_agent="wazeyes")


'''

1.

Receber o endereço, por voz ou texto,
e gerar um arquivo json no servidor,
com o endereço que foi digitado ou falado

2.

Realizar a leitura do arquivo json (entrada.json)
que armazena o endereço,
e escrever em outro arquivo (saida.json)
que são as coordenadas geográficas

3.

Irá consumir o arquivo (saida.json)
dentro de um tempo
irá gerar uma rota que será exibida ao portador da necessidade especial
somente quando ele ativar o botão "iniciar trajeto"

'''

entrada = ler_arquivo("entrada_json.json")


opção = chamarMenu()

while opção > 0 and opção < 4:
    if opção == 1:
        print(registrar(entrada, "entrada_json.json"))

    elif opção == 2:

        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="wazeyes")

        endereço = input(
            "Para confirmar digite um endereco com número e cidade. (Exemplo: avenida paulista, 100 São Paulo) : ")

        resultado = geolocator.geocode(endereço)
        print("--------------------------------")
        print("\nEndereço completo.: ", resultado)
        print("\nCoordenadas.......: ", resultado.latitude, resultado.longitude)

    elif opção == 3:

        latitude = float(input("Digite a latitude...: "))
        longitude = float(input("Digite a longitude.: "))
        valid_address = True
        resultado = geolocator.reverse(f"{latitude}, {longitude}")

        print("Endereço completo.: ", resultado)
