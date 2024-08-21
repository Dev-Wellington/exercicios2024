inicio = int(input("Digite o início do intervalo: "))
final = int(input("Digite o final do intervalo: "))

resultado = int()

for numeros in range(inicio, final + 1):
    if numeros % 3 == 0  and numeros % 5 == 0:
        continue
    elif numeros % 3 == 0:
        resultado += numeros
    else: numeros % 5 == 0
    resultado -= numeros
    

    