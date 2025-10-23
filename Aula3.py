ATIVIDADE2

1----------------------------------------------------------------------------------------

valor = int(input("Digite um número inteiro: "))
antecessor = valor - 1
print("O antecessor de",valor,"é",antecessor)

2----------------------------------------------------------------------------------------

base = float(input("Adicione a base do retângulo: "))
altura = float(input("Adicione a base do retângulo: "))

calculo = base * altura

print("A área do seu retângulo é", calculo,"cm²")

3----------------------------------------------------------------------------------------

eleitores= int(input("coloque o numero de eleitores"))
brancos = int(input("coloque o numero de votos brancos"))
nulos = int(input("coloque o numero de votos nulos"))
validos = int(input("coloque o numero de votos validos"))
brancos = (brancos / eleitores) * 100
nulos = (nulos / eleitores) * 100
validos = (validos / eleitores) * 100
print("o numero de eleitores é: ", eleitores)
print("o percentual de votos brancos é: ", brancos)
print("o percentual de votos nulos é: ", nulos)
print("o percentual de votos validos é: ", validos)

4----------------------------------------------------------------------------------------

anos = int(input("Adicione a quantidade de anos: "))
meses = int(input("Adicione a quantidade de meses: "))
dias = int(input("Adicione a quantidade de dias: "))

total = (anos * 365) + (meses * 30) + dias

print("A idade total em dias é: ",total)

5----------------------------------------------------------------------------------------

def soma_imposto(taxa_imposto, custo):
  custo_com_imposto = custo * (1 + taxa_imposto / 100)
  return custo_com_imposto

taxa = int(input("Qual o valor da taxa?"))
preco_original = int(input("Qual valor padrão do produto?"))
preco_final = soma_imposto(taxa, preco_original)
print("O custo final com imposto é:", preco_final)

6----------------------------------------------------------------------------------------

def sextaquestao():
    total_pagas = 0
    qtd_pagas = 0

    while True:
        valor_prestacao = float(input("Digite o valor da prestação ou 0 para encerrar programa: "))

        if valor_prestacao == 0:
            break

        dias_atraso = int(input("Digite o número de dias de atraso: "))
        if dias_atraso == 0:
         valor_total = valor_prestacao
        else:
            multa = valor_prestacao * 0.03
            juros = valor_prestacao * 0.001 * dias_atraso
            valor_total = valor_prestacao + multa + juros

        print("Valor a ser pago: R$", valor_total)

        total_pagas += valor_total
        qtd_pagas += 1

    print("RELATÓRIO DO DIA:")

    print("Quantidade de prestações pagas:",qtd_pagas)
    print("Valor total pago: R$",total_pagas)
