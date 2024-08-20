palavra = str(input("Digite sua frase favorita: ")).upper().replace(" ", "")
palavra_invertida = str()

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

print(palavra_invertida)

if palavra == palavra_invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

print(palavra)