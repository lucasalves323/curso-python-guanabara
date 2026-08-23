# Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
mai = men = 0

while True:
    dados.append(str(input('Informe seu nome: ')))
    dados.append(float(input('Informe seu peso (Kg): ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = (str(input('Você deseja continuar? [S/N] ')))
    if opcao in 'Nn':
        break

print(f'A) O total de pessoas cadastradas foi {len(pessoas)}.')
print(f'B) O maior peso registrado foi de {mai} Kg. Quem chegou a esse peso foi: ')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'C) O menor peso registrado foi de {men} Kg. Quem pesou assim foi:')        
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')