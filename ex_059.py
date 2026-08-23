# Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
acao = 0
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
while acao != 5:
    sleep(2)
    print('-=' * 14)
    print('\33[7;40mESTE É O SEU MENU DE AÇÕES: \33[m')
    print('-=' * 14)
    print('''[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa''')
    acao = int(input('\33[1;33mQual é a sua ação?\33[m '))
    if acao == 1:
        print(f'O resultado de {n1} + {n2} é {n1 + n2}.')
        print('\33[1;31mTente outra ação!\33[m')
    elif acao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}.')
        print('\33[1;31mTente outra ação!\33[m')
    elif acao == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}.')
            print('\33[1;31mTente outra ação!\33[m')
        else:
            print(f'O maior número é o {n2}.')
            print('\33[1;31mTente outra ação!\33[m')
    elif acao == 4:
        print('Informe novos números:')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif acao == 5:
        print('Fim do programa!')
    else:
        print('Opção inválida! Tente novamente.')