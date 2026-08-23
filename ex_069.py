# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final mostre:
# a) Quantas pessoas tem mais de 18 anos;
# b) Quantos homens foram cadastrados;
# c) Quantas mulheres tem menos de 20 anos.

homens = 0
mulheres20 = 0
pessoas18 = 0
total = 0

while True:
    print('=' * 30)
    print('CADASTRE UMA PESSOA')
    print('=' * 30)
    idade = int(input('Informe a idade: '))
    sexo = ' '
    total += 1
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).upper()[0].strip()
    if idade >= 18:
        pessoas18 += 1
    if idade < 20 and sexo == 'F':
        mulheres20 += 1
    if sexo == 'M':
        homens += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''Ao total {total} pessoas se cadastraram. 
Dessas, {homens} são homens; 
{pessoas18} do total tem mais de 18 anos.
E {mulheres20} é o número de mulheres com menos de 20 anos.''')
