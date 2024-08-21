numero = int(input("Digite um número: "))
soma = 0

for n in range(1, numero  ):
    if numero % n == 0:
        soma += n
   

if soma == numero:
    print(f"{numero} é um número perfeito")
else:
    print(f"{numero} não é um número perfeito")
        


