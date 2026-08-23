# Faça um algorítimo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
desconto = (preco * 0.05)

print(f'O produto que custava R${preco:.2f}, na promoção com 5% de desconto está custando R${preco - desconto:.2f}.')