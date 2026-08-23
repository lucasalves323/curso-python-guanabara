# Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.

'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa (Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}Kg.')
print(f'O menor peso foi de {menor}Kg.')
'''

lista = []  #lista vazia
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    lista += [peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lista))  #maximo valor da lista
print('O Menor peso foi:', min(lista))  #minimo valor da lista
