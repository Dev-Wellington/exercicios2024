numeros = list()

for i in range (1, 4):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    for indice_atual in range(len(numeros) - 1):
        if numeros[indice_atual] > numeros[indice_atual + 1]:
            numeros[indice_atual], numeros[indice_atual + 1] = numeros[indice_atual + 1], numeros[indice_atual]

print(numeros)