# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) quantos números foram digitados. b) a lista de valores, ordenada
# de forma decrescente. c) se o valor 5 foi digitado e está ou não lista.

lista = []


while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Você deseja continuar digitando? [S/N] '))
    if opcao in 'Nn':
        break
lista.sort(reverse=True)
print('=' * 40)
print(f'Ao todo foram digitados {len(lista)} números.')
print(f'A lista em ordem decrescente é {lista}.')
if 5 in lista:
    print(f'O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
