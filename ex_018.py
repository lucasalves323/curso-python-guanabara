# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo
"""
import math

n = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))

print(f'O ângulo de {n} tem o SENO de {sen:.2f}, COSSENO de {cos:.2f} e TANGENTE de {tg:.2f}.')
"""

from math import sin, cos, tan, radians

n = float(input('Digite o valor do ângulo: '))
sen = sin(radians(n))
coss = cos(radians(n))
tg = tan(radians(n))

print(f'O ângulo de {n} tem o SENO de {sen:.2f}, COSSENO de {coss:.2f} e TANGENTE de {tg:.2f}.')
