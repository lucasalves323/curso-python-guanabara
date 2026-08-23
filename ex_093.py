# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.

dados = dict()
gols = list()
dados['Nome'] = str(input('Nome do Jogador: '))
dados['Partidas'] = int(input(f'Quantidade de partidas jogadas por {dados['Nome']}: '))
for p in range(1, dados['Partidas'] + 1):
     gols.append(int(input(f'Informe a quantidade de gols na: {p}ª partida: ')))
     dados['Gols'] = gols.copy()
dados['Total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas.')
for p, g in enumerate(gols):
     print(f'  => Na partida {p+1}, fez {g} gols.')
print(f'Fazendo um total de {dados["Total"]} gols.')
