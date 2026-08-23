# Crie um programa que leia números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre elas (desconsiderando o flag).

cont = 0
soma = 0
'''
while n != 999:
    n = int(input('Digite um número inteiro. [Digite 999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
print(f'Foram digitados {cont} números e a soma deles deu {soma}.')'''

while True:
    n = int(input('Digite um número inteiro. [Digite 999 para parar.]: '))
    if n == 999:
        break  
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma deles deu {soma}.')       