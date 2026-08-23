# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.
from time import sleep
print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)


reta1 = float(input('Qual o comprimento da primeira reta? '))
reta2 = float(input('Qual o comprimento da segunda reta? '))
reta3 = float(input('Qual o comprimento da terceira reta? '))

print('ANALISANDO TRÂNGULOS...')
sleep(1)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Sim! É possível formar um triângulo.')
else:
    print('É impossível formar um triângulo!')