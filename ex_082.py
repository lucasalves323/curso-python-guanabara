# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

listaCompleta = []
listaPares = []
listaImpares = []

while True:
    n = int(input('Digite um número: '))
    if n not in listaCompleta:
        listaCompleta.append(n)
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)
    opcao = str(input('Você deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print(f'A lista completa dos números digitados é {listaCompleta}.')
print(f'A lista dos números pares digitados é {listaPares}.')
print(f'A lista dos números ímpares digitados é {listaImpares}.')
    