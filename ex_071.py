# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (int)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs.: Considere que o caixa possui cédulas de 50, 20, 10 e 1 real.
'''from random import choice
valor = int(input('Qual o valor do saque? R$ '))
total = valor
cedula = 50
totalCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break'''

valor = int(input("Quanto você quer sacar? R$"))

for cedula in [50, 20, 10, 1]:
    quantidade = valor // cedula 
    valor %= cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula}")