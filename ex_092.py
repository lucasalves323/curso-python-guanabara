# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
# diferente de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos
# a pessoa vai se aposentar.
from datetime import date
worker = dict()
worker['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
worker['Idade'] = date.today().year - nascimento
worker['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if worker['CTPS'] == 0:
    print('-=' * 30)
    for k, v in worker.items():
        print(f'{k} tem o valor {v}.')
else:
    worker['Contratação'] = int(input('Ano de contratação: '))
    worker['Salário'] = float(input('Salário R$: '))
    worker['Aposentadoria'] = worker['Idade'] + ((worker['Contratação'] + 35) - date.today().year)
    print('-=' * 30)
    for k, v in worker.items():
        print(f'{k} tem o valor {v}.')
