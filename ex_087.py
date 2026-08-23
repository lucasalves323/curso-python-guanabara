# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados:
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0
terceira = 0

for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}: '))        
print('-=' * 30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('-=' * 30)
for linha in range (0, 3):
    soma_coluna += matriz[linha][2]
for coluna in range (0, 3):
    if coluna == 0:
        maior = matriz[1][0]
    else:
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]

print(f'A) A soma dos números pares deu: {soma_pares}.')   
print(f'B) A soma dos valores da terceira coluna deu: {soma_coluna}.')
print(f'C) O maior número da segunda linha é: {maior}.')






      
