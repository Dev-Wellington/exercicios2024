def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def par_impar(numero):
    if numero % 2 == 0:
       return False        
    else:
        return True

def divisivel_por_quatro(numero):
    if numero % 4 == 0:
        return True
    return False

inicio = int(input("Digite o primeiro numero do intervalo: "))
final = int(input("Digite o numero final do intervalo : "))


for numeros in range(inicio,final +1):
    soma_digitos = 0
    resultado = False

    for digitos in str(numeros):
        soma_digitos += int(digitos)

    if par_impar(soma_digitos):
        resultado = True

    if divisivel_por_quatro(numeros) and primo(numeros) and resultado:
        print(f'O numero {numeros} é um numero magico')
        break
    else:
        print(f'Infelizmente nenhum numero magico foi encontrado')
        break

