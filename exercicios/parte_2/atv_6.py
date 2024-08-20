vogais = ['a', 'e', 'i', 'o', 'u']
frase = str(input("Digite sua frase favorita: ")).lower()
c = 0
for vogal in frase:
    if vogal in vogais:
        c += 1
    
print(f"A frase tem {c} vogais.")