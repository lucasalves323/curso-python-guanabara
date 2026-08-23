# Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(0.5)
    for c in valores:
        print(c, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    mai = 0
    for v in valores:
        if len(valores) == 0:
            mai = v
        else: 
            if v > mai:
                mai = v
    print(f'O maior valor informado foi {mai}.')

maior(0, 3, 5, 1)
maior(2, 3, 1)
maior(0, 5, 10, 6, 3, 9)
maior(2, 7)
maior()
