inicio = int(input("Digite o início do intervalo: "))
final = int(input("Digite o final do intervalo: "))

resultado = 0

for numeros in range(inicio, final + 1):
    if numeros % 3 == 0  and numeros % 5 == 0:
        continue
    if numeros % 3 == 0:   
        resultado += numeros   
    if numeros % 5 == 0:
        resultado -= numeros
       

print(f'O valor calculado foi: {resultado}')

