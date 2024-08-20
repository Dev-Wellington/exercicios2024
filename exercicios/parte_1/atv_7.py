compras = list()

while True:
    produto = input('Digite o nome do produto ou "mostrar" para mostar sua lista de compras: ')
    if produto == 'mostrar':
        break
    compras.append(produto)



print('Lista de compras:')
print(compras)