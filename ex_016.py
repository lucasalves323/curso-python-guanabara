# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.

from math import trunc
n = float(input('Digite um número: '))

print(f'A porção inteira do número "{n}" é {trunc(n)}')
