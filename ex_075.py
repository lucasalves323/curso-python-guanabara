# Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9. b) em que posição foi digitado
# o primeiro valor 3. c) quais foram os números pares.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))

num = n1, n2, n3, n4
pares = []

print(f'Você digitou os valores {num}.')
print(f'a) O valor 9 apareceu {num.count(9)}x.')
if 3 in num:
    print(f'b) O primeiro valor "3" foi digitado na posição {num.index(3) + 1}.')
else:
    print('b) O valor 3 não foi digitado em nenhum momento.')
print(f'c) Os números pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
        
