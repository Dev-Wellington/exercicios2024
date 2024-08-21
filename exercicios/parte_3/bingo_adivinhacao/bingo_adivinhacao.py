import random

cartela = list()
sorteios = 0

for aleatorio in range(1,6):
    cartela.append(random.randint(1,75))

print(f'Sua cartela é : {cartela}') 

while True:
    numero = random.randint(1,75)

    if numero in cartela:
        print(f'O número sorteado foi: {numero} e você acertou !!!')
        while numero in cartela:
            cartela.remove(numero)
        print(f'Sua cartela está assim: {cartela}')
    else:
        print(f'O número sorteado foi: {numero}')

    sorteios +=1

    if not cartela:
        print(f'Parabéns ! , você completou em {sorteios} sorteios.')
        break

#forma do jogador escolher o numero
'''
while True:
    numero = int(input('Digite um numero'))

    if numero in cartela:
        print(f'O número sorteado foi: {numero} e você acertou !!!')
        while numero in cartela:
            cartela.remove(numero)
    else:
        print(f'O número sorteado foi: {numero}')

    sorteios +=1

    if not cartela:
        print(f'Parabéns ! , você completou em {sorteios} sorteios.')
        break
'''

