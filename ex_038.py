# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# - Primeiro valor é maior.
# - Segundo valor é maior.
# - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('Não existe valor maior, os dois números são \33[1miguais!\33m')
elif n1 > n2:
    print('O \33[1;31mprimeiro\33[m valor é maior.')
else:
    print('O \33[1;31msegundo\33[m valor é maior.')
