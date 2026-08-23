# Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo. Seu programa tem que realizar
# 3 contagens através da função criada:
# a) de 1 até 10, de 1 em 1:
# b) de 10 até 0, de 2 em 2:
# c) uma contagem personalizada:

# A FORMA QUE EU FIZ MISTURANDO FOR COM DEF

from time import sleep
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1: ')
for c in range(1, 11):
    print(c, end=' ')
    sleep(0.5)
print('FIM!')
print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2: ')
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(0.5)
print('FIM!')

def contador(a, b, c):
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for c in range(a, b, c):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))

if i > f:
    if p >= 0:
        p = p * -1
    f = f - 1
if i < f:
    f = f + 1
    print('Resposta inválida para a opção "Passo".')
contador(i, f, p)

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)