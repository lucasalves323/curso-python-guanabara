# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
jogador = int(input('Em qual número você pensou? '))

print('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print(f'Parabéns, você acertou! Eu também pensei no número {computador}.')
else:
    print(f'Você errou! Eu pensei no número {computador}.')
print('==FIM==')
