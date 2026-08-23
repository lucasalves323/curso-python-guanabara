# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados de forma tabular.

'''produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)


print('=' * 50)
print(f'{"LISTAGEM DE PREÇO":^50}')
print('=' * 50)

for p in range(0, len(produtos), 2):
    print(f'{produtos[p]:.<40}', end='')
    print(f'R${produtos[p + 1]:>7}')
print('=' * 50)'''


produtos = ('Feijão', 6.75, 'Arroz', 4.50, 'Coca-Cola', 11.80, 'Pão', 4, 'Óleo', 5.30, 
            'Fuba', 3.20, 'Leite', 6.45, 'Picanha', 45)

for p in produtos:
    if type(p) is str:
        print(f'{p:.<40}', end= '')
    else:
        print(f'R$ {p:>5.2f}')