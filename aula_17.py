num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(num)

num.append(7)
print(num)

num.insert(0, 3)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.remove(2) #remove apenas o primeiro número 2
print(num)

if 9 in num:
    num.remove(9)
else:
    print('O número 9 não foi encontrado')

num.pop()
print(num)

num.pop(3)
print(num)

print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c}, está o número {v}.')
print('Final da lista')

valores = []

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')

a = [2, 3, 4, 7]
b = a
# se eu quiser trocar um número em uma das listas, eu vou acabar mudando
# nas duas, pois eu já igualei as duas listas. Ex.:
b[2] = 8
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')
# contudo há como modificar um valor em apenas uma lista:
b = a[:] # aqui significa que ele está copiando todos os itens de a.