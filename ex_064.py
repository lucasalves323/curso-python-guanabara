# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles. (desconsiderando o flag).

print('=' * 52)
print('SOMANDO NÚMEROS ALEATÓRIOS. PARA PARAR DIGITE "999": ')
print('=' * 52)
soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número qualquer [999 para parar]: '))
    if n != 999:
        soma += n 
        cont += 1
print(f'A soma dos {cont} números digitados foi {soma}.')
