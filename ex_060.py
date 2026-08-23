# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120.

from math import factorial
n = int(input('Você deseja o fatorial de qual número? '))
f = factorial(n)
print(f'O fatorial do número {n} é {f}.')

n = int(input('Você deseja o fatorial de qual número? '))
contador = n
fatorial = 1
print(f'Calculando {n}! = ', end='')
while contador > 0:
    print(contador, end='') 
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador -= 1
print(fatorial)

n = int(input('Você deseja o fatorial de qual número? '))
fatorial = 1
for c in range(n, 0, -1):
    fatorial = fatorial * c
print(fatorial)
