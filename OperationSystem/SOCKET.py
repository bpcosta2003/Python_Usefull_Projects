import socket

resp = 'S'

while resp == 'S':
    url = input("Digite uma URL : ")
    ip = socket.gethostbyname(url)
    print("O IP referente à URL informada é : ", ip)
    print(socket.getservbyname("domain"))
    print(socket.getservbyname("http"))
    print(socket.getservbyname("ftp"))
    resp = input("Digite < S > para continuar : ").upper()
