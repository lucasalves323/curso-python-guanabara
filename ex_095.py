# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.

# Agora devemos fazer com que o programa funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.
from time import sleep
dados = {}
gols = []
jogadores = []
while True:
    gols.clear()
    dados['Nome'] = str(input('Informe o nome do jogador: '))
    dados['Partidas'] = int(input(f'Informe quantas partidas {dados['Nome']} jogou: '))
    for g in range(1, dados['Partidas']+1):
        gols.append(int(input(f'Quantos gols {dados["Nome"]} fez na {g}ª partida? ')))
        dados['Gols'] = gols.copy() 
        dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    while True:
        opcao = str(input('Você deseja registrar outro jogador? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite "S" ou "N".')
    if opcao == 'N':
        break
print('-=' * 30)
print(jogadores)
print(f'{'Cod':<5}{'Nome':<15}{'Partidas':<15}{'Gols':<15}{'Total':>5}')
print('-' * 60)
for k, v in enumerate(jogadores):
    print(f'{k:<5}', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()

while True:
    print('=' * 60)
    escolha = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {escolha}!')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {jogadores[escolha]['Nome']}:')
        for j, g in enumerate(jogadores[escolha]["Gols"]):
            sleep(1)
            print('   ', end='')
            print(f'No {j+1}º jogo fez {g} gols.')
print('>> PROGRAMA ENCERRADO <<')
        



