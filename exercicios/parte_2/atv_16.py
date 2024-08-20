texto = str(input("Digite uma palavra: ")).upper()
inverso = list()

for letra in texto:
    inverso.insert(0,letra)

print(inverso)