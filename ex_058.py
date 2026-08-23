# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint
from time import sleep

print('Olá, eu sou o seu computador. Vamos jogar um jogo?')
print('Você tem que adivinhar em qual número estou pensando de 0 a 10.')
pc = randint(0, 10)
pessoa = int(input('Em qual número eu estou pensando? '))
palpites = 1
while not pc == pessoa:
    print('Hum...')
    sleep(1)
    if pc > pessoa:
        pessoa = int(input('Você errou. Tente um número maior: '))
        palpites += 1
    else:
        pessoa = int(input('Você errou. Tente um número menor: '))
        palpites += 1
print('Hum...') 
sleep(1)   
if palpites <= 2:
    print(f'Uau! Como você sabia? Também pensei no número {pc}.')
    print(f'Você só precisou de {palpites} palpites para acertar!')
elif palpites >= 3 and palpites <= 5:
    print(f'Parabéns. Também pensei no número {pc}.')
    print(f'Mas você ainda precisou de {palpites} palpites para acertar.')
else:
    print(f'Ok. Também pensei no número {pc}.')
    print(f'Mas com toda minha ajuda você ainda precisou de {palpites} palpites para acertar. Rsrsrs')
