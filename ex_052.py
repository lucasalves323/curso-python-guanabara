# Faça um programa que leia um número inteiro e diga se ele é ou não
# número primo.

n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n +1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print(f'O número {c} é primo!')
else:
    print(f'O número {c} não é primo.')


'''
n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m')
        tot += 1
    else:
        print('\033[31m')
    print(c, end='')
    
print(f'O número {n} foi divisível {tot} vezes.')

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')
'''
