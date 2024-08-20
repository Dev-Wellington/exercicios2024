soma = 0 
media = 0


while True:
    nota = float(input("Digite a nota ou -1 para parar: "))
    if nota == -1:
        break    
    media += 1
    soma += nota
   


print(f'A média das notas é {soma / media}')