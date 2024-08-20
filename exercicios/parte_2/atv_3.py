peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura no formato 0.00 : "))


def IMC(peso, altura):
    return peso / (altura ** 2)


print(f'Seu IMC atual é {IMC(peso, altura)} ')