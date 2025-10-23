ATIVIDADE

1----------------------------------------------------------------------------------------------

arroz = int(input("Coloque o valor do arroz: "))
feijao = int(input("Coloque o valor do feijao: "))
carne = int(input("Coloque o valor do carne: "))
macarrao = int(input("Coloque o valor do macarrao: "))

arroz_media = 9
feijao_media = 12
carne_media  = 30
macarrao_media  = 5

if arroz > arroz_media:
  print("Valor na media!")
else:
  print("Valor acima da media!")

if feijao > feijao_media:
  print("Valor na media!")
else:
  print("Valor acima da media!")

if carne > carne_media:
  print("Valor na media!")
else:
  print("Valor acima da media!")

if macarrao > macarrao_media:
  print("Valor na media!")
else:
  print("Valor acima da media!")

2----------------------------------------------------------------------------------------------

valor = int(input("Adicione um numero: "))
if valor % 2 == 0:
  print(valor, "é um número par!")
else:
  print(valor, "não é um número impar!")

if valor > 0:
  print(valor, "é um número positivo.")
elif valor < 0:
  print(valor, "é um número negativo.")
else:
  print(valor, "é zero.")

3----------------------------------------------------------------------------------------------

nota1 = int(input("Adicione a primeira nota: "))
nota2 = int(input("Adicione a segunda nota: "))
nota3 = int(input("Adicione a terceira nota: "))

total = (nota1 + nota2 + nota3)/3

if total >= 10
 print("Aprovado com Louvor!")
else:
  print("Reprovado!")

if total > 7
 print("Aprovado!")
else:
  print("Reprovado!")

4----------------------------------------------------------------------------------------------

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (5 * (fahrenheit - 32)) / 9

print("Temperatura em Fahrenheit: ", fahrenheit)
print("Temperatura convertida em Celsius :", celsius)

5----------------------------------------------------------------------------------------------

num_votantes = int(input("Digite o número total de votantes: "))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(num_votantes):
  voto = int(input(f"Voto do eleitor {i+1} (1, 2 ou 3): "))
  if voto == 1:
    votos_candidato1 += 1
  elif voto == 2:
    votos_candidato2 += 1
  elif voto == 3:
    votos_candidato3 += 1
  else:
    print("Voto inválido. Por favor, vote 1, 2 ou 3.")
    # Optionally, you could ask the voter to vote again or skip this vote.
    # For simplicity, we'll just acknowledge the invalid vote and continue.

print("Resultado da eleição:")
print("Candidato 1: ", votos_candidato1, "votos")
print("Candidato 1: ", votos_candidato2, "votos")
print("Candidato 1: ", votos_candidato3, "votos")

6----------------------------------------------------------------------------------------------

zsfasfaepessoas = int(input("quantas pessoas deseja ver: "))
maior = 0
menor = 100
soma_mulheres = 0
cont_mulheres = 0
cont_homens = 0

for i in range(pessoas):
    print(f"Pessoa {i+1}:")
    altura = float(input("Digite a altura: "))
    sexo = input("Digite o sexo: ")

    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

    if sexo:
        soma_mulheres += altura
        cont_mulheres += 1
    elif sexo:
        cont_homens += 1
    else:
        print("Sexo inválido. Contando como outro.")


if cont_mulheres > 0:
  media_mulheres = soma_mulheres / cont_mulheres
else:
  media_mulheres = 0


total_pessoas= cont_mulheres + cont_homens
if total_pessoas > 0:
  porc_homens = (cont_homens / total_pessoas) * 100
  porc_mulheres = (cont_mulheres / total_pessoas) * 100
else:
  porc_homens = 0
  porc_mulheres = 0


print("Maior altura:", maior)
print("Menor altura:", menor)
print("Média de altura das mulheres:", media_mulheres)
print("Número total de homens:", cont_homens)
print("Porcentagem de homens:", porc_homens, "%")
print("Porcentagem de mulheres:", porc_mulheres, "%")

7----------------------------------------------------------------------------------------------

valorpvendas = float(input("Insira o valor projetado de vendas "))
lucroanual = valorpvendas*0.23
print("O lucro anual é: ",lucroanual)

8----------------------------------------------------------------------------------------------

num = int(input("Digite um número inteiro: "))

if num <= 1:
    print(num,"não é primo.")
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(num,"é primo!")
    else:
        print(num,"não é primo.")

9----------------------------------------------------------------------------------------------

import math

numero = int(input("Insira um valor inteiro: "))
fatorial = math.factorial(numero)
print("O fatorial desse número é:", fatorial)

10----------------------------------------------------------------------------------------------

valor_original = int(input("Digite o valor original do produto: "))
desconto = int(input("Digite a porcentagem de desconto: "))

valor_desconto = (valor_original * desconto) / 100

preco_final = valor_original - valor_desconto

print("Valor original: R$",valor_original)
print("Desconto aplicado:",desconto)
print("Valor do desconto: R$",valor_desconto)
print("Preço final do produto: R$",preco_final)

11----------------------------------------------------------------------------------------------

horas = float(input("Digite o tempo em horas: "))

minutos = horas * 60
segundos = horas * 3600

print("Tempo informado:",horas,"horas")
print("Equivalente em minutos:", minutos,"minutos")
print("Equivalente em segundos:", segundos,"segundos")

12----------------------------------------------------------------------------------------------

n1 = int(input("Adicione o valor da primeira nota "))
p1 = int(input("Adicione o peso da primeira nota "))
n2 = int(input("Adicione o valor da segunda nota "))
p2 = int(input("Adicione o peso da segunda nota "))
n3 = int(input("Adicione o valor da terceira nota "))
p3 = int(input("Adicione o peso da terceira nota "))

media = (n1*p1+n2*p2+n3*p3)/(p1+p2+p3)
print("A média ponderada deu: ", media)

13----------------------------------------------------------------------------------------------

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]

print("Números em ordem crescente:")
for num in numeros:
    print(num)

14----------------------------------------------------------------------------------------------

forma = input("Insira qual forma você quer calcular a área: (quadrado, retangulo, circulo, triangulo)").lower()
if forma == "quadrado":
  lado = int(input("Insira o valor de um dos lados do quadrado: "))
  area = lado * lado
  print("A área do quadrado é: ", area)
elif forma == "retangulo":
  base = int(input("Insira o valor da base: "))
  altura = int(input("Insira o valor da altura: "))
  area = base * altura
  print("A área do retangulo é: ", area)
elif forma == "circulo":
  raio = int(input("Insira o valor do raio: "))
  area = 3.14 * (raio ** 2)
  print("A área do circulo é: ", area)
elif forma == "triangulo":
  base = int(input("Insira o valor da base: "))
  altura = int(input("Insira o valor da altura: "))
  area = (base * altura) / 2
  print("A área do triangulo é: ", area)
