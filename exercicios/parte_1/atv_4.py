temperatura = float(input("Digite a temperatura :"))

if temperatura > 30:
    print("O dia de hoje ta quente ♨")
if temperatura < 15:
    print("O dia de hoje ta frio ❄")
if temperatura > 15 and temperatura <= 30:
    print("O dia de hoje ta agradável ☀")