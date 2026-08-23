# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$ 1000.
# c) Qual é o nome do produto mais barato.

total = cont = produtosMais = menorPreco= 0
nomeMaisBarato = ' '


while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o valor do produto R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        produtosMais += 1
    if cont == 1 or preco < menorPreco:
        nomeMaisBarato = nome
        menorPreco = preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{'FIM DO PROGRAMA' :=^40}')
print(f'''O total de produtos infomados foi {cont}.
O valor da compra deu R$ {total:.2f}
Dos produtos informados, {produtosMais} está acima de R$ 1.000,00.
O produto mais barato é o {nomeMaisBarato}.''')

