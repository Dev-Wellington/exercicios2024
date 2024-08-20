soma = 0
num = int(input("Digite um número: "))
 

while num != 0:
    soma += num
    num = int(input("digite 0 para sair ou outro número para continuar: "))
   
        
print("A soma dos números digitados é:", soma)
