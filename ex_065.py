# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valor lido. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

maior = 0
menor = 0
soma = 0
cont = 0
resposta = 'S'

while resposta in 'Ss':
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n  
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
print(f'A média entre todos os {cont} valores digitados é {soma / cont:.2f}.')
print(f'O maior valor lido é {maior}.')
print(f'O menor valor lido é {menor}.')




