def soma(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def divisao(n1,n2):
    return n1 / n2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada: ")

if operacao == '+':
    print(soma(num1,num2))

if operacao == '-':
    print(subtracao(num1,num2))

if operacao == '*':
    print(multiplicacao(num1,num2))

if operacao == '/':
    print(divisao(num1,num2))