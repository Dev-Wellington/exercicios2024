numeros = list()

numero = int()

while True:
    numero = int(input("Digite um número para adiciona-lo na lista e -1 para parar: "))
    if numero == -1:
        break
    numeros.append(numero)
    numeros.sort()

print(f'O menor numero é {numeros[0]} o maior numero é {numeros[-1]} e a média é {sum(numeros)/len(numeros)}')