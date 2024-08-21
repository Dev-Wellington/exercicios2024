n = int(input("Digite o valor do numero: "))

inicio = [0, 1]
for i in range(2, n):
    proximo = inicio[i-1] + inicio[i-2] 
    inicio.append(proximo) 


fibo = [inicio[i] for i in range(n)]

print(f"Os primeiros {n} números da sequência de Fibonacci são: {fibo}")

#print(f"Os primeiros {n} números da sequência de Fibonacci são: {inicio[:n]}")