# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = []
pares = []
somados = []
print(f'Sorteando 5 valores da lista: ', end='') 
def sorteia(*valores):
    for c in valores:
        sleep(0.5)
        print(f'{c}', end=' ')
        numeros.append(c)
for s in range(0, 5):        
    sorteia(randint(1, 10)) 
print('PRONTO!')
def somaPar(*numbers):
    soma = 0
    for c in numbers:
        if c % 2 == 0:
            soma += c
            pares.append(c)
    somados.append(soma)
somaPar(*numeros)
print(f'Somando os valores pares de {numeros}, temos {somados}.')
