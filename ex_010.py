# Crie um programa que leia quanto dinheiro uma pessoa tem 
# na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 5.00

n = float(input('Digite quantos reais você tem na carteira: R$ '))
dolar = 3.27
poderCompra = (n / dolar)

print(f'Você pode consegue comprar US$ {poderCompra:.1f}')