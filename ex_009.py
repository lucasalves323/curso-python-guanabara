# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))
i = 0

while i <= 10:
    print(f'{n} x {i} = {n * i}')
    i = i + 1

