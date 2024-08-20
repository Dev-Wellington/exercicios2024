
def par(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    

numero = int(input("Digite um número: "))

print(par(numero))
