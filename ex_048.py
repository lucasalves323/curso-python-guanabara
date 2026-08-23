# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c3 in range(3, 501, 3):
    if c3 % 2 == 1:
        soma += c3
        cont += 1
print(f'A soma dos {cont} números no intervalo de 1 a 500 é {soma}')
