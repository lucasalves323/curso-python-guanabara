# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais.
# - ISÓSCELES: dois lados iguais, um diferente.
# - ESCALENO: todos os lados diferentes.
from time import sleep
lado1 = float(input('Medida do lado 1: '))
lado2 = float(input('Medida do lado 2: '))
lado3 = float(input('Medida do lado 3: '))

print('~' * 30)
print('ANALISANDO TRIÂNGULOS...')
print('~' * 30)
sleep(1)

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print('ERRO! É impossível fazer um triângulo com essas medidas.')
elif lado1 == lado2 == lado3:
    print('Esse é um triângulo EQUILÁTERO!')
elif lado1 != lado2 != lado3 != lado1:
    print('Esse é um triângulo ESCALENO!')
else:
    print('Esse é um triângulo ISÓSCELES!')