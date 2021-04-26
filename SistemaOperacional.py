from datetime import datetime
import getpass
import platform

print("--------------------------------\n")
print("Distribuição do Sistema Operacional.: ", platform.platform())
print("\nNome do Sistema Operacional.........: ", platform.system())
print("\nVersão do Sistema Operacional.......: ", platform.release())
print("\nArquitetura.........................: ", platform.architecture())
print("\nNome do Computador..................: ", platform.node())
print("\nTipo de Máquina.....................: ", platform.machine())
print("\nProcessador.........................: ", platform.processor())
print("\nVersão do Python....................: ", platform.python_version())


print("\nUsuário.......: ", getpass.getuser())
print("\nData Completa.: ", datetime.now())
print("\nDia...........: ", datetime.now().day)
print("\nMês...........: ", datetime.now().month)
print("\nAno...........: ", datetime.now().year)
print("\nHora..........: ", datetime.now().hour)
print("\nMinuto........: ", datetime.now().minute)
print("\nSegundo.......: ", datetime.now().second)


usuario = input("\nDigite o usuário: ").upper()
senha = getpass.getpass("\nDigite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("\nUsuário logado")
else:
    print("\nLogin Negado")
