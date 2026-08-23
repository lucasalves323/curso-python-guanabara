# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
"""
UMA FORMA

from math import sqrt

co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
hp = sqrt(co ** 2 + ca ** 2)

print(f'O cateto oposto vale {co}, e o cateto adjacente vale {ca},')
print(f'logo, a hipotenusa vale {hp:.2f}.')

OUTRA FORMA

co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
hp = (co ** 2 + ca ** 2) ** (1/2)

print(f'O cateto oposto vale {co}, e o cateto adjacente vale {ca},')
print(f'logo, a hipotenusa vale {hp:.2f}.')
"""
from math import hypot

co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
hp = hypot(co, ca)

print(f'O cateto oposto vale {co}, e o cateto adjacente vale {ca},')
print(f'logo, a hipotenusa vale {hp:.2f}.')

