# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. b) os últimos 4. c) Times em ordem alfabética
# d) em que posição está o time do Náutico.

times = ('São Bernardo', 'Náutico', 'Sport', 'Vila Nova', 'Fortaleza', 'Goiás',
         'Novorizontino', 'CRB', 'Criciúma', 'Athletic', 'Ceará SC', 'Juventude',
         'Operário', 'Atlético-GO', 'Avaí', 'Cuiabá', 'Botafogo SP', 'Londrina',
         'Ponte Preta', 'América-MG')

print('=' * 42)
print('ANALISANDO A TABELA DO BRASILEIRÃO SÉRIE B')
print('=' * 42)

print(f'a) Os 5 primeiros colocados são: {times[0:5]}.')
print('=' * 100)
print(f'b) Os últimos 4 colocados são: {times[-4:]}.')
print('=' * 100)
print(f'c) Os times em ordem alfabética é: {sorted(times)} ')
print('=' * 100)
print(f'd) O time do náutico está na {times.index('Náutico') + 1}ª posição.')