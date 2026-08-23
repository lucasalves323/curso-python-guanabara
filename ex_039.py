# Faça um program que leia o ano de nascimento de um jovem e informe
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou
# que passou do prazo.
from datetime import date
print('=' * 38)
print(f'\33[7;42mBEM VINDO AO ALISTAMENTO MILITAR {date.today().year}!\33[m')
print('=' * 38)

ano = int(input('Digite o ano do seu nascimento: '))
idade = (date.today().year - ano)
falta = 18 - idade
atraso = idade - 18

if idade == 18:
    print('Excelente! Esse ano você tem idade para se alistar. Seja bem vindo!')
elif idade < 18:
    print(f'Esse ano você faz {idade} anos, ainda faltam {falta} anos para o seu alistamento.')
    print(f'Seu alistamento será em {falta + date.today().year}.')
else:
    print(f'Você já tem {idade} anos, você já está {atraso} anos atrasado.')
    print(f'Seu alistamento foi em {date.today().year - atraso}.')   
