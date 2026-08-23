# Desenvolva um programa que leia seis números inteiros e mostra a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsider-o
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
       soma += n
       cont += 1
print(f'Foram digitados {cont} números pares que somam: {soma}.') 