import random

numero_minimo = int(input('Qual o numero minimo do intervalo?\n'))
numero_maximo = int(input('Qual o numero máximo do intervalo?\n'))

tentativas = int(input('Quantas tentativas para acertar?\n'))

numero_sorteado = random.randint(numero_minimo, numero_maximo)

while True: 
  tentativa = int(input(f'Digite um numero entre {numero_minimo} e {numero_maximo}.\n'))

  if tentativa == numero_sorteado:
    print('Parabéns você acertou o numero.')
    break
  else:
    tentativas -= 1  #tentativas = tentativas - 1
    if tentativas == 0:
      print(f'Você não acertou o número e não tem mais tentativas. O número era {numero_sorteado}')
      break
    else:
      print(f'Número errado. Tente novamente. Você ainda tem {tentativas} tentativas.')