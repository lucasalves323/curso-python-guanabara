# Crie um programa que faça o computador jogar Jokenpô com você.
# ESSA FOI A FORMA FEITA POR MIM

from random import choice
from time import sleep

print('*' * 36)
print('VAMOS JOGAR PEDRA, PAPEL OU TESOURA?')
print('*' * 36)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(lista)
print('''Escolha uma das opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
voce = int(input('Sua jogada: '))
print('PEDRA')
sleep(1)
print('PAPEL OU')
sleep(0.5)
print('TEEE...')
sleep(1)
print('...SOURA!')

print('-=' * 30)
if voce == 1:
    if pc == 'PEDRA':
        print(f'Eu também escolhi {pc}. Empatamos. Vamos de novo!')
    elif pc == 'PAPEL':
        print(f'Yes! Eu escolhi {pc}. E papel embrulha pedra. \33[1;31mVocê perdeu!\33[m')
    else:
        print(f'Droga! Eu escolhi {pc}. Pedra quebra a tesoura. \33[1;32mVocê venceu!\33[m')
elif voce == 2:
    if pc == 'PEDRA':
        print(f'Droga! Eu escolhi {pc}. E papel embrulha pedra. \33[1;32mVocê venceu!\33[m')
    elif pc == 'PAPEL':
        print(f'Eu também escolhi {pc}. Empatamos. Vamos de novo!')
    else:
        print(f'Yes! Eu escolhi {pc}. E tesoura corta papel. \33[1;31mVocê perdeu!\33[m')
elif voce == 3:
    if pc == 'PEDRA':
        print(f'Yes! Eu escolhi {pc}. E pedra quebra a tesoura. \33[1;31mVocê perdeu!\33[m')
    elif pc == 'PAPEL':
        print(f'Droga! Eu escolhi {pc}. A tesoura corta o papel. \33[1;32mVocê venceu!\33[m')
    else:
        print(f'Eu também escolhi {pc}. Empatamos. vamos de novo!')
else:
    print('Opção inválida. Tente novamente.')
print('-=' * 30)
