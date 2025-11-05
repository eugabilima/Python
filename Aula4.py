1-----------------------------------------------------------------------

cor = input("Adicione uma cor entre: 'verde', 'amarelo' ou 'vermelho' ")

def checar_semaforo(cor):

  if cor == "verde":
    return "Siga!"
  elif cor == "amarelo":
    return "Atenção!"
  elif cor == "vermelho":
    return "Pare!"
  else:
    return "Cor inválida."

print(checar_semaforo(cor))

2-----------------------------------------------------------------------

imc = float(input("adicione seu peso em (kg): "))

def classificar_imc(imc):

  if imc < 18.5:
    return "Abaixo do peso"
  elif 18.5 <= imc < 24.9:
    return "Peso normal"
  elif 25.0 <= imc < 29.9:
    return "Sobrepeso"
  else:
    return "Obesidade"

print(classificar_imc(imc))

3-----------------------------------------------------------------------

renda = float(input("entre com sua renda: "))
score = int(input("digite o numero do credito: "))

def checar_elegibilidade(renda, score):
    if renda >= 5000 and score >= 700:
        return "Cartão Premium Elegível"
    elif renda >= 2000 and score >= 600:
        return "Cartão Standard Elegível"
    else:
        return "Não elegível no momento."


print(checar_elegibilidade(renda,score))

4-----------------------------------------------------------------------

temp = int(input("Adicione a temperatura: "))

def sugerir_roupa(temp):

  if temp >= 30:
    return "Muito calor! Use roupas leves. ☀️"
  elif 18 <= temp < 30:
    return "Clima agradável. Uma camiseta e calça são ideais. 👕"
  else:
    return "Está frio. Vista um casaco! 🧥"


print(sugerir_roupa(temp))

5-----------------------------------------------------------------------

placar_time_a = float(input("qual o placar do time a"))
placar_time_b = float(input("qual o placar do time b"))

def verificar_vencedor():

 if placar_time_a>placar_time_b:
  print("TIME A VENCEUUU")
 elif placar_time_b>placar_time_a:
  print("TIME B VENCEUUU")
 else: 
  print("EMPATE!")

verificar_vencedor()

6-----------------------------------------------------------------------

dia_da_semana = input("Qual o dia da semana: ")

dia1 = "domingo"
dia2 = "segunda"
dia3 = "terça"
dia4 = "quarta"
dia5 = "quinta"
dia6 = "sexta"
dia7 = "sabado"

def tipo_de_dia(dia_da_semana):

  if dia_da_semana == dia1:
    return "Fim de Semana! 🎉"
  elif dia_da_semana == dia7:
    return "Fim de Semana! 🎉"
  else:
    return "Dia Útil. 💼"


print(tipo_de_dia (dia_da_semana))

7-----------------------------------------------------------------------

valor_pedido = float(input("Qual o valor do pedido? "))

def calcular_frete(valor_pedido):

  if valor_pedido >= 80:
    return valor_pedido
  else:
    return valor_pedido + 10

print(calcular_frete(valor_pedido))

8-----------------------------------------------------------------------

estrelas = int(input("Classifique as estrelas de 1 a 5: "))

def  classificar_avaliacao(estrelas):

  if estrelas == 5:
    return "Excelente!"
  elif estrelas == 4:
    return "Muito Bom."
  elif estrelas == 3:
    return "Satisfatório."
  else:
    return "Insatisfatório."

print(classificar_avaliacao(estrelas))

9-----------------------------------------------------------------------

