

def format_number(number):
    if number < 0: #@ condição para não aceitar números negativos
        print("Valor negativo. INVÁLIDO")
    else: 
        toString = str(number) #@ Passo o valor para string 

        formatado = list(toString.split()[0]) #@ Pego o valor da string e separo cada valor, o [0] é para separar cada indice. 100 = ['1','0','0'] 

        for i in range(len(formatado))[::-3][1:]: #@ Crio um loop com o lenght da lista acima. O [::-3] é para percorrer de tras para frente a cada 3 valores. O [1:] pula o primeiro índice, como está invertido, vai plar o último

            formatado.insert(i+1,",") #@ para cada 3 casas de trás para frente adiciona a ','. O 'i' está pegando uma casa antes, por isso +1 

        final = "".join(formatado) #@ vai juntar todos os valores da lista com "".
        print('"' + final + '"')

valor = input("Insira um valor positivo : ")
format_number(int(valor))
