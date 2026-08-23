# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
corrente = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if corrente - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo {maior} pessoas atingiram a maioridade e {menor}, não.')