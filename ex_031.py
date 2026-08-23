# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens
# de até 200km e R$ 0,45 para viagens mais longas.

from time import sleep
distancia = float(input('Qual a distância da viagem em Km? '))
print('PROCESSANDO...')
sleep(1)

if distancia <= 200:
    print(f'A passagem custa R$ {distancia * 0.5:.2f}.')
else:
    print(f'A passagem custa R$ {distancia * 0.45:.2f}.')
print('Tenha uma excelente viagem!')