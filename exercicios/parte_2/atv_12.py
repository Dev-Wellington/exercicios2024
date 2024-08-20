import random
numero = int()
aleatorio = random.randint(1, 100)


while numero != aleatorio:
    numero = int(input("Digite um número: "))
    if numero > aleatorio:
        print(f"O número que você quer encontrar é menor que {numero} ")
    if numero < aleatorio:
        print(f"O número que você quer encontrar é maior que {numero}")

print(f'Parabéns!!! você acertou o número secreto era {aleatorio} ')
