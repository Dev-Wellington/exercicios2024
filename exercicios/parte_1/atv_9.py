
frase = str(input("Digite sua frase favorita: ")).upper()
repetida = str(input("Digite a letra que deseja contar: ")).upper()


c = frase.count(repetida)
print(f"A letra {repetida} aparece {c} vezes na frase.")


c = 0
for letra in frase:
    if letra == repetida:
        c += 1
        
print(f"A letra {repetida} aparece {c} vezes na frase.")