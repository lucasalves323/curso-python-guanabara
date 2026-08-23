# Faça um programa que leia um número de 0 a 9999 e mostre
# na tela cada um dos dígitos separados.

n = int(input('Digite um número de 0 a 9999: '))

if (n < 0) or (n > 9999):
    print('Número não válido.')

else:
    num = str(n)
    if len(num) == 4:

        print(f'Analisando o número {num}...')
        print('Esse número possui: ')
        print(f'Unidade: {num[3]}')
        print(f'Dezena: {num[2]}')
        print(f'Centena: {num[1]}')
        print(f'Milhar: {num[0]}')

    elif len(num) == 3:

        print(f'Unidade: {num[2]}')
        print(f'Dezena: {num[1]}')
        print(f'Centena: {num[0]}')
        print('Milhar: 0')

    elif len(num) == 2:

        print(f'Unidade: {num[1]}')
        print(f'Dezena: {num[0]}')
        print('Centena: 0')
        print('Milhar: 0')
    
    elif len(num) == 1:

        print(f'Unidade: {num[0]}')
        print('Dezena: 0')
        print('Centena: 0')
        print('Milhar: 0')
        