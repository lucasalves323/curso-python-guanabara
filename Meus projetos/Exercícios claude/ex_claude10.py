"""
Crie uma classe Time com nome e pontos = 0. Implemente um método marcar_ponto(self, adversario) que sorteia aleatoriamente (random.choice) entre self e adversario pra decidir quem ganha o ponto da rodada, e incrementa o pontos do sorteado. Crie um loop no main que simula 5 rodadas entre dois times, chamando esse método repetidamente, e ao final mostra o placar.
"""
import random

class Time:

    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos
        

    def marcar_ponto(self, adversario):
        times = [self, adversario]
        vencedor = random.choice(times)
        vencedor.pontos += 1
        print(f'O {vencedor.nome} marcou um ponto!')


nautico = Time('Náutico')
sport = Time('Sport')
lista = [nautico, sport]

for rodada in range(1, 6):
    print(f'Na {rodada}ª rodada')
    nautico.marcar_ponto(sport)

print(f'A MD5 terminou com o placar de {sport.pontos} para o Sport e {nautico.pontos} para o náutico.')
