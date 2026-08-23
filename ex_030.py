# Crie um programa que leia um número inteiro e mostre na tela
# se ele é PAR ou ÍMPAR.
from time import sleep
n = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1)

if n % 2 == 0:
    print('Esse número é par!')
else:
    print('Esse número é ímpar!')