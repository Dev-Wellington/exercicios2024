numero = int(input("Digite um número: "))
soma = 0

for i in range(1, numero + 1):
    soma += i

print(f"A soma dos primeiros, {numero}primeiros números naturais é: {soma}")