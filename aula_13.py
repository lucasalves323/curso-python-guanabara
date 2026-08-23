"""
for c in range(1, 7): # ELE NÃO CONSIDERA O ÚLTIMO NÚMERO. 

#para contagem regressiva:

for c in range(6, 0, -1):
    print(c)
print('FIM')

# para contar de 2 em 2:

for c in range (0, 7, 2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
"""
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s = s + n # tbm pode ser escrito: s += n
print(f'O somatório de todos os valores foi {s}')