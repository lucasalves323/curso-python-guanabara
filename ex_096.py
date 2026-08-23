# Faça um programa que tenha uma função chamada área(), que receba 
# as dimensões de um terreno retangular (largura e comprimento) e 
# mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}m x {comp}m é de {a:.2f}m²')

print('   Controle de Terrenos   ')
print('-' * 27)    
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)

