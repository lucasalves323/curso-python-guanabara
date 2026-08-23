# Crie um programa que faça o computador jogar Jokenpô com você.
# ESSA FOI A FORMA FEITA POR GUANABARA

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura') 
pc = randint(0, 2)
print('''Escolha uma das opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[pc]}.')
print('-=' * 11)
#if pc == 0:
#if jogador == 0: