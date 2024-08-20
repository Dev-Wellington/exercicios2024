
inicio_intervalo = int(input("Digite o início do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))
primos = list()

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


for i in range(inicio_intervalo, fim_intervalo + 1):
    if primo(i):
        primos.append(i)


print(primos)
