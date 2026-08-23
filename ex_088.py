# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.

'''from random import randint
lista = list()
resultado = list()
jogos = int(input('Quantos jogos você deseja realizar? '))
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    resultado.append(lista[:])
    lista.clear()
    total += 1

print(resultado)'''


from random import randint
lista = list()
resultado = list()
jogadas = int(input('Quantas jogadas você deseja realizar? '))

for i in range(0, jogadas):
    for c in range(0, 6):
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
    resultado.append(lista[:])
    lista.clear()
print(f'Os jogos realizados foram: ')
for j, l in enumerate(resultado):
    print(f'Jogo {j + 1}: {l} ')