# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores pares e ímpares em
# ordem crescente.

# A FORMA QUE EU FIZ
'''dados = list()
pares = []
impares = []

for c in range (0, 7):
    dados.append(int(input(f'Digite o {c + 1}º valor: ')))
for n in dados:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
print(f'Os números pares digitados foram {pares}.')
print(f'Os números ímpares digitados foram {impares}.')'''

# A FORMA QUE GUANABARA FEZ
num = [[], []]
valor = 0

for c in range (1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}.')
print(f'Os valores ímpares digitados foram: {num[1]}.')