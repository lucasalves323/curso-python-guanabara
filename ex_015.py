# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quas ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$ 0,15 por Km rodado.

km = float(input('Quantos quilômetros rodados? '))
dias = int(input('Quantos dias alugados: '))
preco = 0.15 * km + 60 * dias

print(f'Para um aluguel de {dias} dias, percorrendo {km}km, o total a pagar é R${preco:.2f}.')