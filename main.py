def Nome():
    nome = input("Entre com o seu nome: ")
    print("Bem vindo", nome)
Nome()
-----------------------------------------------------------------------------------------------
def Salario():
    salario = float(input("Entre com salario do mes: "))
    print("Seu salario é R$", salario)
Salario()
-----------------------------------------------------------------------------------------------
def Soma():
    valor1= int(input("Entre com o valor 1: "))
    valor2= int(input("Entre com o valor 2: "))
    soma = valor1 + valor2
    print(soma)
Soma()
-----------------------------------------------------------------------------------------------
def Menu():
    print("Opção do Menu")
    print("Para Acessar escolha 1: ")
    print("Para sair escolha 0: ")
    escolha = int(input("Escolha: "))
    return Acesso()

def Acesso():
    print("Bem Vindo")
------------------------------------------------------------------------------------------------
def Menu():
    print("Opção do Menu")
    print("Para Acessar escolha 1: ")
    print("Para sair escolha 0: ")
    escolha = int(input("Escolha: "))
    return Acesso()

def Acesso():
    print("Bem Vindo")

Menu()
Acesso()
------------------------------------------------------------------------------------------------
def Acesso():
    print("Bem Vindo")

def Menu():
    print("Opção do Menu")
    print("Para Acessar escolha 1: ")
    print("Para sair escolha 0: ")
escolha = int(input("Escolha: "))
if escolha == 1:
    Acesso()
elif escolha == 0:
    print("Saiu")
else:
    print("Não é possivel acessar")
