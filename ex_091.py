# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor 
# tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = ()
print('VALORES SORTEADOS: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
# o 'sorted' está ordenando valores do 'jogo'. Portanto, jogo.items()
# o itemgetter se for parte (0), ele coloca em ordem as keys, se for (1) ele bota em ordem os valores
print('-=' * 30)
print('== RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
