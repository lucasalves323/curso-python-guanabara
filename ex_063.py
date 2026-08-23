# Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma sequência de Fibonacci.
# Exemplo: 0-1-1-2-3-5-8
print('SEQUÊNCIA DE FIBONACCI')
print('~' * 22)
n = int(input('Quantos elementos você quer ver? '))

anterior = 1
retrasado = 0
cont = 0
print('0, 1, ', end='')
while cont < n - 2:
    soma = anterior + retrasado
    print(f'{soma},', end=' ')
    cont += 1
    retrasado = anterior
    anterior = soma
print('FIM!')    
print(f'O total de elementos da sequência foi {cont + 2}.')